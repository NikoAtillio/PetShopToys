from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', views.products, name='products'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
    path('payment/', include('payment.urls')), 
    path('shop/', include('shop.urls')),  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
