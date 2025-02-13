from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('products/', views.product_list, name='products'),
    path('<slug:pet_type_slug>/', views.product_list, name='product_list_by_pet_type'),
    path('<slug:pet_type_slug>/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),

    path('checkout/', views.checkout, name='checkout'),
]
