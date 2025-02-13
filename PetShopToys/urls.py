from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from shop import views as shop_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('productscat/', views.productscat, name='productscat'),
    path('productsdog/', views.productsdog, name='productsdog'),
    path('shop/', include(('shop.urls', 'shop'), namespace='shop')),
    path('payment/', include(('payment.urls', 'payment'), namespace='payment')),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('shop/', include('shop.urls', namespace='shop')),  # Make sure this line exists
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)