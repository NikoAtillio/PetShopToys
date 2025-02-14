# shop/urls.py
from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.product_list, name='product_list'),  # Root shop URL
    path('products/', views.product_list, name='products'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('products/search/', views.search_products, name='search_products'),
    path('cats/', views.product_list, {'pet_type_slug': 'cats'}, name='cats_products'),
    path('dogs/', views.product_list, {'pet_type_slug': 'dogs'}, name='dogs_products'),
    path('<slug:pet_type_slug>/', views.product_list, name='product_list_by_pet_type'),
    path('<slug:pet_type_slug>/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
]