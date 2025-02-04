from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.urls import reverse
from .models import PetType, Category, Product
import stripe
from django.conf import settings
from shop.models import Product

# Create your views here.

def product_list(request, pet_type_slug=None, category_slug=None):
    pet_type = None
    category = None
    pet_types = PetType.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if pet_type_slug:
        pet_type = get_object_or_404(PetType, slug=pet_type_slug)
        categories = categories.filter(pet_type=pet_type)
        products = products.filter(category__pet_type=pet_type)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug, pet_type=pet_type)
        products = products.filter(category=category)
    return render(request, 'products.html', {
        'pet_type': pet_type,
        'category': category,
        'pet_types': pet_types,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {
        'product': product
    })

def shop_home(request):
    return render(request, 'shop_home.html')

def productsdog(request):
    return render(request, 'products/productsdog.html')

def productscat(request):
    return render(request, 'products/productscat.html')

def checkout(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        context = {
            'product': product,
        }
        return render(request, 'checkout.html', context)
    else:
        return render(request, 'checkout.html')
    
    
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
