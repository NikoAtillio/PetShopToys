from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from PetShopToys import views

from PetShopToys import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.home, name='home'),
    path('payment/', views.payment, name='payment'),
    path('shop/', include('shop.urls')),
    path("accounts/", include("allauth.urls")),  
] 
+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
