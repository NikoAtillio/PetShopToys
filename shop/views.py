from django.shortcuts import render, get_object_or_404
from .models import PetType, Category, Product

# Create your views here.

def product_list(request, pet_type_slug=None, category_slug=None):
    pet_type = None
    category = None
    pet_types = PetType.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if pet_type_slug:
        pet_type = get_object_or_404(PetType, slug=pet_type_slug)
        categories = categories.filter(pet_type=pet_type)
        products = products.filter(category__pet_type=pet_type)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug, pet_type=pet_type)
        products = products.filter(category=category)
    return render(request, 'products.html', {
        'pet_type': pet_type,
        'category': category,
        'pet_types': pet_types,
        'categories': categories,
        'products': products
    })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {
        'product': product
    })

def shop_home(request):
    return render(request, 'shop_home.html')

def productsdog(request):
    return render(request, 'products/productsdog.html')

def productscat(request):
    return render(request, 'products/productscat.html')


