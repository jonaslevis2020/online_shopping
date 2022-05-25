from tkinter.tix import Tree
from colorama import Fore, Style, init
from django.shortcuts import get_object_or_404, redirect, render
from store.models import Product

from cart.models import Cart, CartItem

# Create your views here.

init(autoreset=True)

def get_cart_id(request):
    cart_id = request.session.session_key
    print(Style.BRIGHT+Fore.CYAN+'cart id ==> '+Fore.YELLOW+f'{cart_id}')
    if not cart_id:
        cart_id = request.session.create()
    return cart_id


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    stock = product.stock
    check_stock = False
    print(Style.BRIGHT+Fore.CYAN+f'passed product id ==> '+Fore.YELLOW+f'{product_id}')
    print(Style.BRIGHT+Fore.CYAN+f'real product id ==> '+Fore.YELLOW+f'{product.id}')
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=get_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        cart_item.quantity += 1
        cart_item.save()
        print(Style.BRIGHT+Fore.CYAN+'cart_item product id ==> '+Fore.YELLOW+f'{cart_item.product.id}')
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
        print(Style.BRIGHT+Fore.CYAN+'cart_item product id ==> '+Fore.YELLOW+f'{cart_item.product.id}')

    if stock >= cart_item.quantity:
        check_stock = True
    if check_stock:
        return redirect('cart')
    else:
        quantity = cart_item.quantity
        context = {
            'check_stock': check_stock,
            'stock': stock,
            'quantity': quantity,
            'product':Product,
        }
        return render(request, 'store/stock_warning.html', context)


def remove_cart(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    print(Style.BRIGHT+Fore.CYAN+'passed product id ==> '+Fore.YELLOW+f'{product_id}')
    print(Style.BRIGHT+Fore.CYAN+'real product id ==> '+Fore.YELLOW+f'{product.id}')
    if cart_item.quantity>1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

def remove_cart_item(request, product_id):
    cart = Cart.objects.get(cart_id=get_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    print(Style.BRIGHT+Fore.CYAN+'passed product id ==> '+Fore.YELLOW+f'{product_id}')
    print(Style.BRIGHT+Fore.CYAN+'real product id ==> '+Fore.YELLOW+f'{product.id}')
    cart_item.delete()
    return redirect('cart')



def get_cart(request):
    total = 0
    quantity = 0
    cart_items = []
    items_count = 0
    tax = 0
    grand_total = 0
    context = {}
    try:
        cart = Cart.objects.get(cart_id=get_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)
        items_count = cart_items.count()
        for cart_item in cart_items:
            total += (cart_item.product.price*cart_item.quantity)
            quantity += cart_item.quantity
        tax = (2*total)/100
        grand_total = total+tax
    except Exception as e:
        print(Fore.RED+f'{e.args}')
    context = {
        'total':total,
        'tax':tax,
        'grand_total':grand_total,
        'cart_items': cart_items,
        'quantity': quantity,
        'items_count': items_count,
    }
    return render(request, 'store/cart.html', context)
