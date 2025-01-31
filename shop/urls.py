from django.urls import path
from . import views  # Import views from the shop app

urlpatterns = [
    path('', views.shop_home, name='shop_home'),  # Shop homepage
    path('dogs/', views.dog_products, name='dog_products'),
    path('cats/', views.cat_products, name='cat_products'),
]
