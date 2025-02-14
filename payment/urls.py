from django.urls import path, include
from . import views

app_name = 'payment'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('create-stripe-checkout-session/', views.create_stripe_checkout_session, name='create_stripe_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('test/', views.test, name='test'),
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
]