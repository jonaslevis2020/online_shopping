from cart.models import CartItem, Cart
from cart.views import get_cart_id
from category.models import Category
from django.shortcuts import get_object_or_404, render

from store.models import Product

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
    is_cart_item = False
    p = get_object_or_404(Product, slug=product_slug)
    cart_id = get_cart_id(request)
    cart = Cart.objects.filter(cart_id=cart_id)
    cart_items = CartItem.objects.filter(cart=cart[0])
    category_slug = category_slug
    for item in cart_items:
        if item.product.id == p.id:
            is_cart_item = True
    context = {
        'p': p,
        'category_slug': category_slug,
        'is_cart_item': is_cart_item,
        }
    return render(request, 'store/product_detail.html', context)
