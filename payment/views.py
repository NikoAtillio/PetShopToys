from django.shortcuts import render, redirect
import stripe
from django.conf import settings
# Create your views here.

stripe.api_key = settings.STRIPE_API_KEY

def create_checkout_session():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': 'T-shirt',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://success.html',
        cancel_url='http://cancel.html',
        customer_email=user_email,
    )
