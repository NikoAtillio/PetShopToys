from django.shortcuts import render, get_object_or_404
from .models import PetType, Category, Product
import logging

logger = logging.getLogger(__name__)

def product_list(request, pet_type_slug=None, category_slug=None):
    pet_type = None
    category = None
    pet_types = PetType.objects.all()
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if pet_type_slug:
        pet_type = get_object_or_404(PetType, slug=pet_type_slug)
        products = products.filter(pet_type=pet_type)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug, pet_type=pet_type)
        products = products.filter(category=category)

    logger.debug(f"Products found: {products.count()}")
    return render(request, 'shop/products.html', {
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
    return render(request, 'shop/shop_home.html')