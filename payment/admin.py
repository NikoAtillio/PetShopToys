from django.contrib import admin
from .models import UserPayment    
# Register your models here.

@admin.register(UserPayment)
class UserPaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'stripe_customer_id', 'stripe_checkout_session_id', 'stripe_product_id', 'product_name', 'quantity', 'price', 'currency', 'has_paid']
    list_filter = ['has_paid']
    list_editable = ['has_paid']
    ordering = ['-payment__payment_date']  