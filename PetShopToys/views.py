from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def productsdog(request):
    return render(request, 'productsdog.html')

def productscat(request):
    return render(request, 'productscat.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def payment(request):
    return render(request, 'checkout.html')
