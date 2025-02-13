from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class UserPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=100)
    stripe_checkout_session_id = models.CharField(max_length=100)
    stripe_product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=100)
    has_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.product_name} - Paid: {self.has_paid}"

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'User Payment'
        verbose_name_plural = 'User Payments'