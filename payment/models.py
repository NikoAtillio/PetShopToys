from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Payment(models.Model):
#     payment_id = models.CharField(max_length=100)
#     payment_status = models.CharField(max_length=100)
#     payment_method = models.CharField(max_length=100)
#     payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     payment_currency = models.CharField(max_length=100)
#     payment_description = models.TextField()
#     payment_receipt_url = models.URLField()
#     payment_date = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.payment_id
    
#     class Meta:
#         ordering = ['-payment_date']
        

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
    
    def __str__(self):
        return f"{self.user.username} - {self.product_name} - Paid: {self.has_paid}"
    
    # class Meta:
    #     ordering = ['-payment__payment_date']
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField(max_length=200)