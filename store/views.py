from unicodedata import category
from django.shortcuts import get_list_or_404, get_object_or_404, render

from store.models import Product
from category.models import Category

# Create your views here.


def store(request, category_slug=None):
    products = ''
    category = category_slug
    if category:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(category=category, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)
    # categories = Category.objects.all()
    context = {
        'products': products,
        'total': products.count(),
        'category':category,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    p = get_object_or_404(Product, slug=product_slug)
    category_slug = category_slug
    context = {
        'p': p,
        'category_slug': category_slug,
        }
    return render(request, 'store/product_detail.html', context)