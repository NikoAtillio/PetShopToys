from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
import stripe
from django.conf import settings
from .models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        
        successurl = request.build_absolute_uri(reverse('success'))
        cancelurl = request.build_absolute_uri(reverse('cancel'))
   
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': product.name,
                        },
                        'unit_amount': int(product.price * 100),  # Stripe expects the amount in cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=successurl,
            cancel_url=cancelurl,
        )

        return redirect(checkout_session.url)
    else:
        return redirect('productscat')  # or another relevant page


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


def test(request):
    return HttpResponse('test')
