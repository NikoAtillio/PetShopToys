from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.contrib import messages
import stripe
from django.conf import settings
from shop.models import Product
from .models import Cart, CartItem
import logging

logger = logging.getLogger(__name__)

stripe.api_key = settings.STRIPE_SECRET_KEY

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('shop:product_detail', id=product.id, slug=product.slug)

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('payment:cart_detail')

def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'payment/cart.html', {'cart_items': cart_items, 'cart': cart})

def cart_items_count(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        return {'cart_items_count': cart.cartitem_set.count()}
    return {'cart_items_count': 0}

def clear_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    CartItem.objects.filter(cart=cart).delete()
    return redirect('payment:cart_detail')


def checkout(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product_slug = request.POST.get('product_slug')

        logger.debug(f"Checkout attempted - ID: {product_id}, Slug: {product_slug}")

        try:
            product = get_object_or_404(Product, id=product_id)

            # Store product information in session
            request.session['selected_product_id'] = product_id
            request.session['selected_product_slug'] = product.slug

            logger.debug(f"Product found for checkout: {product.name}")

            context = {
                'product': product,
            }
            return render(request, 'checkout.html', context)

        except Product.DoesNotExist:
            logger.error(f"Product not found - ID: {product_id}")
            messages.error(request, "Product not found or unavailable")
            return redirect('shop:productscat')

    return redirect('shop:productscat')

def create_stripe_checkout_session(request):
    if request.method == "POST":
        product_id = request.session.get('selected_product_id')

        logger.debug(f"Creating Stripe session for product ID: {product_id}")

        try:
            product = get_object_or_404(Product, id=product_id, available=True)

            successurl = request.build_absolute_uri(reverse('payment:success'))
            cancelurl = request.build_absolute_uri(reverse('payment:cancel'))

            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'gbp',
                            'product_data': {
                                'name': product.name,
                            },
                            'unit_amount': int(product.price * 100),
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=successurl,
                cancel_url=cancelurl,
            )

            # Store checkout session ID
            request.session['checkout_session_id'] = checkout_session.id

            logger.debug(f"Stripe session created successfully for {product.name}")
            return redirect(checkout_session.url)

        except Exception as e:
            logger.error(f"Error creating Stripe session: {str(e)}")
            messages.error(request, f"Error processing payment: {str(e)}")
            return redirect('shop:productscat')

    return redirect('shop:productscat')

def success(request):
    # Clear session data
    if 'selected_product_id' in request.session:
        del request.session['selected_product_id']
    if 'selected_product_slug' in request.session:
        del request.session['selected_product_slug']
    if 'checkout_session_id' in request.session:
        del request.session['checkout_session_id']

    messages.success(request, "Payment successful! Thank you for your purchase.")
    return render(request, 'success.html')

def cancel(request):
    messages.warning(request, "Payment was cancelled.")
    return render(request, 'cancel.html')

def test(request):
    return HttpResponse('test')