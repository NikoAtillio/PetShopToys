from django.urls import path
from .views import PaymentView, PaymentSuccessView, PaymentCancelView, PaymentErrorView, PaymentWebhookView, home

urlpatterns = {
    path('', home, name='home'),
    path('payment/', PaymentView.as_view(), name='payment'),
    path('payment/success/', PaymentSuccessView.as_view(), name='payment_success'),
    path('payment/cancel/', PaymentCancelView.as_view(), name='payment_cancel'),
    path('payment/error/', PaymentErrorView.as_view(), name='payment_error'),
    path('payment/webhook/', PaymentWebhookView.as_view(), name='payment_webhook'),
}