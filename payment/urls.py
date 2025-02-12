from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('create-stripe-checkout-session/', views.create_stripe_checkout_session, name='create_stripe_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('test/', views.test, name='test'),
]