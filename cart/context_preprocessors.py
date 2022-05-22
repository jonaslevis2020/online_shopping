from cart.models import Cart
from cart.models import CartItem
from .views import  get_cart_id


def get_cart_items(request):
    cart_id = get_cart_id(request)
    print(f'cart_id ===> {cart_id}')
    cart = Cart.objects.filter(cart_id=cart_id)
    cart_items = CartItem.objects.all().filter(cart=cart[0])
    cart_items_count = cart_items.count()
    return {'cart_items_count': cart_items_count}
