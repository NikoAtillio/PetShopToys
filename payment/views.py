from django.shortcuts import render, redirect
import stripe
from django.conf import settings
# Create your views here.



stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session():
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='success.html',
            cancel_url='cancel.html',
    )

    return redirect(checkout_session.url, code=303)
