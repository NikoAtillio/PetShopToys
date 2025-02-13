from django.shortcuts import render, get_object_or_404
from .models import PetType, Category, Product
import logging, Category, PetType

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
    return render(request, 'products/products.html', {
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
    # Fetch all available dog products by product name
    products = Product.objects.filter(
        available=True,
        name__icontains='Dog'  # This will match any product with 'Dog' in the name
    )
    logger.debug(f"Dog products found: {products.count()}")
    return render(request, 'products/productsdog.html', {'products': products})

def productscat(request):
    # Fetch all available cat products by product name
    products = Product.objects.filter(
        available=True,
        name__icontains='Cat'  # This will match any product with 'Cat' in the name
    )
    logger.debug(f"Cat products found: {products.count()}")
    return render(request, 'products/productscat.html', {'products': products})


def list_all_products(request):
    products = Product.objects.all().select_related('category')
    return render(request, 'list_products.html', {'products': products})