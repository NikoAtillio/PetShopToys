from django.shortcuts import render

# Create your views here.
def shop_home(request):
    return render(request, 'shop_home.html')

def dog_products(request):
    return render(request, 'dogs/dog_products.html')

def cat_products(request):
    return render(request, 'cats/cat_products.html')