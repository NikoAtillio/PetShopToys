from django.urls import path
from . import views

urlpatterns = {
    path('checkout/', views.checkout, name='checkout'),
    path('payment/success/', views.success, name='payment_success'),
    path('payment/cancel/', views.cancel, name='payment_cancel'),
}