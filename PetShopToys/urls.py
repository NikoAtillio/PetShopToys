from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'),
    path('shop/', include('shop.urls', namespace='shop')),
    path('payment/', include('payment.urls', namespace='payment')),
    path('accounts/', include('allauth.urls')),  
    
    # Custom user authentication for both authentication systems (Django and Django-allauth)
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)