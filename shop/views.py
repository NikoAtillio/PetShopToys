from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import PetType, Category, Product
import logging

logger = logging.getLogger(__name__)

def product_list(request, pet_type_slug=None):
    try:
        # Initialize variables
        pet_type = None
        category = None

        # Get all pet types and categories, ordered alphabetically
        pet_types = PetType.objects.all()
        categories = Category.objects.all().order_by('name')

        # Start with all available products
        products = Product.objects.filter(available=True)

        # Filter by pet type if specified
        if pet_type_slug:
            pet_type = get_object_or_404(PetType, slug=pet_type_slug)
            products = products.filter(pet_type=pet_type)
            # Filter categories to show only those that have products for this pet type
            categories = Category.objects.filter(
                products__pet_type=pet_type
            ).distinct().order_by('name')
            logger.info(f"Filtered by pet type: {pet_type.name}, found {products.count()} products")

        # Get category from query parameter
        category_slug = request.GET.get('category')
        if category_slug:
            # Remove the get_object_or_404 and directly filter products
            category = Category.objects.filter(slug=category_slug).first()
            if category:
                products = products.filter(category=category)
                logger.info(f"Filtered by category: {category.name}, found {products.count()} products")

        # Sort products by name
        products = products.order_by('name')

        context = {
            'pet_type': pet_type,
            'category': category,
            'pet_types': pet_types,
            'categories': categories,
            'products': products,
            'products_count': products.count()
        }

        logger.debug(f"Context prepared: {len(products)} products, "
                    f"Pet type: {pet_type.name if pet_type else 'All'}, "
                    f"Category: {category.name if category else 'All'}")

        return render(request, 'products/products.html', context)

    except Exception as e:
        logger.error(f"Error in product_list view: {str(e)}")
        return render(request, 'products/error.html', {
            'error_message': "Sorry, there was an error loading the products."
        })

def search_products(request):
    try:
        query = request.GET.get('q', '').strip()
        products = []

        if query:
            # Search in product name and description
            products = Product.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query),
                available=True
            ).order_by('name')

            logger.info(f"Search query: '{query}' found {products.count()} products")

        context = {
            'query': query,
            'products': products,
            'products_count': len(products)
        }

        return render(request, 'search.html', context)

    except Exception as e:
        logger.error(f"Error in search_products view: {str(e)}")
        return render(request, 'search.html', {
            'error_message': "Sorry, there was an error processing your search."
        })
    

    # Product detail/view page

    def product_detail(request, id):
        products = get_object_or_404(Product, id=id)
        return render(request, 'shop/product_detail.html', {'product': product})
