from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
import stripe
from django.conf import settings
# Create your views here.


stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    successurl = 'payment/success/'
    cancelurl = 'payment/cancel/'
   
    checkout_session = stripe.checkout.Session.create(
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

    return redirect('productscat')  # or another relevant page


def success(request):
    return render(request, 'success.html')


def cancel(request):
    return render(request, 'cancel.html')


def test(request):
    return HttpResponse('test')
