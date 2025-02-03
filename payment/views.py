from django.shortcuts import render, redirect
import stripe
from django.conf import settings
# Create your views here.



stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
    )

return redirect(checkout_session.url, code=303


# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
stripe.api_key = 'sk_test_51QnJ47BMzPNz1e4lHz4rrrWTIQJGnlnnpkzrQm5yRR3qThq4taxKZUbwbf4q92fWxAonmYcDOQuOaTYegXgft83w00ClfFfrV0'

def fulfill_checkout(session_id)
  print("Fulfilling Checkout Session", session_id)

  # TODO: Make this function safe to run multiple times,
  # even concurrently, with the same session ID

  # TODO: Make sure fulfillment hasn't already been
  # peformed for this Checkout Session

  # Retrieve the Checkout Session from the API with line_items expanded
  checkout_session = stripe.checkout.Session.retrieve(
    session_id,
    expand=['line_items'],
  )

  # Check the Checkout Session's payment_status property
  # to determine if fulfillment should be peformed
  if checkout_session.payment_status != 'unpaid':
    # TODO: Perform fulfillment of the line items

    # TODO: Record/save fulfillment status for this
    # Checkout Session





def product_view(request):
    return render(request, 'payment/product.html')

def checkout_view(request):
    return render(request, 'payment/checkout.html')