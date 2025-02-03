from django.shortcuts import render, redirect
from django.urls import reverse
import stripe
from django.conf import settings
# Create your views here.


stripe.api_key = settings.STRIPE_SECRET_KEY

def checkout(request):
    successurl = 'payment/success/'
    cancelurl = 'payment/cancel/'
    print(settings.STRIPE_SECRET_KEY)
    print(settings.STRIPE_SECRET_KEY)
    print(settings.STRIPE_SECRET_KEY)
    print(settings.STRIPE_SECRET_KEY)
    print(settings.STRIPE_SECRET_KEY)
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '1QoQDDBTWfUSHSrGSu3cExD2',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=successurl,
            cancel_url=cancelurl,
    )

    return redirect(checkout_session.url, code=303)



def success (request):
    return render(request, 'payment/success.html')


def cancel (request):
    return render(request, 'payment/cancel.html')