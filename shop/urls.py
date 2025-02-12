from django.urls import path
from . import views

app_name = 'shop' 


urlpatterns = [
    path('', views.shop_home, name='shop_home'),
    path('products/', views.product_list, name='products'),
    path('pet/<slug:pet_type_slug>/', views.product_list, name='product_list_by_pet_type'),
    path('pet/<slug:pet_type_slug>/category/<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('product/<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    path('productscat/', views.productscat, name='productscat'),
    path('productsdog/', views.productsdog, name='productsdog'),
]
