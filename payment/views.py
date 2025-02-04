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
                # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                'price': 'price_1QoixVBTWfUSHSrGWhGQ0ESZ',
                'quantity': 1,
            },
            {
                'price': '1QoixzBTWfUSHSrGy6z8jKGd',
                'quantity': 1,
            },
            {
                'price': '1QoiyaBTWfUSHSrGNOKhuGg4',
                'quantity': 1,
            },
            {
                'price': '1Qoiz3BTWfUSHSrGrCiQZUKG',
                'quantity': 1,
            },
            {
                'price': '1QoizaBTWfUSHSrGWyQODZnm',
                'quantity': 1,
            },
            {
                'price': '1QoizuBTWfUSHSrGbVwiYAHe',
                'quantity': 1,
            },
            {
                'price': '1Qoj0LBTWfUSHSrGp5It98mk',
                'quantity': 1,
            },
            {
                'price': '1Qoj0oBTWfUSHSrGbeNZmz78',
                'quantity': 1,
            },
            {
                'price': '1Qoj1CBTWfUSHSrGP8dAIMem',
                'quantity': 1,
            },
            {
                'price': '1QojgvBTWfUSHSrG5wxIP3Wg',
                'quantity': 1,
            },
            {
                'price': '1QojhzBTWfUSHSrGxkQnA8Mq',
                'quantity': 1,
            },
            {
                'price': '1QojiIBTWfUSHSrGYvmG6uQr',
                'quantity': 1,
            },
            {
                'price': '1QojipBTWfUSHSrG8mWpAROi',
                'quantity': 1,
            },
            {
                'price': '1Qojj4BTWfUSHSrGQ9OgKNBl',
                'quantity': 1,
            },
            {
                'price': '1QojjbBTWfUSHSrG1S1QNCbk',
                'quantity': 1,
            },
            {
                'price': '1QojjwBTWfUSHSrGYT3n5rxC',
                'quantity': 1,
            },
            {
                'price': '1QojkJBTWfUSHSrGpeRmCz2S',
                'quantity': 1,
            },
            {
                'price': '1QojkkBTWfUSHSrGRF5pH6Y3',
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url=successurl,
        cancel_url=cancelurl,
    )

    return redirect(checkout_session.url)


def success(request):
    return render(request, 'payment/success.html')


def cancel(request):
    return render(request, 'payment/cancel.html')


def test(request):
    return HttpResponse('test')
