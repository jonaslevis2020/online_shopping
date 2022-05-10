from django.http import HttpResponse
from django.shortcuts import render
from online_shopping.settings import BASE_DIR
from store.models import Product



def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products' : products,
    }
    print(f'BASE_DIR: {BASE_DIR}')
    return render(request, 'home.html', context)

