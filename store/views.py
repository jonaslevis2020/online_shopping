from cart.models import CartItem, Cart
from cart.views import get_cart_id
from category.models import Category
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from colorama import init, Style, Fore
from store.models import Product
from django.db.models import Q
from colorama import init, Style, Fore

# Create your views here.


init(autoreset=True)

def store(request, category_slug=None):
    products = ''
    category = category_slug
    if category:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.all().filter(
            category=category, is_available=True).order_by('-id')
        paginator = Paginator(products, 1)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('-id')
        paginator = Paginator(products, 3)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    print(Style.BRIGHT+Fore.RED+f'Page range ===> {paged_products.paginator.page_range}')
    context = {
        'products': paged_products,
        'total': products.count(),
        'category':category,
    }
    print(Style.BRIGHT+Fore.GREEN+f'Sessiond ID ===> {request.session.session_key}')
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    is_cart_item = False
    p = get_object_or_404(Product, slug=product_slug)
    cart_id = get_cart_id(request)
    cart = Cart.objects.filter(cart_id=cart_id)
    cart_items = CartItem.objects.filter(cart=cart[:1])
    category_slug2 = category_slug
    for item in cart_items:
        if item.product.id == p.id:
            is_cart_item = True
    context = {
        'p': p,
        'category_slug': category_slug2,
        'is_cart_item': is_cart_item,
        }
    return render(request, 'store/product_detail.html', context)


def search(request):
    kw = ''
    if 'keyword' in request.GET:
        kw = request.GET['keyword']
    # if kw != '':
    print(Style.BRIGHT+Fore.MAGENTA+f'keyword: {kw}')
    # if kw:
    products = Product.objects.all().filter(Q(product_name__icontains=kw) | Q(description__icontains=kw))
    # paginator = Paginator(products, 10)
    # page = request.GET.get('page')
    # paged_products = paginator.get_page(page)
    context = {
        'products': products,
        'total': products.count(),
        'keyword': kw,
    }
    return render(request, 'store/store.html', context)
    # else:
    #     return redirect('store')
    # else:
    #     return redirect('store')
