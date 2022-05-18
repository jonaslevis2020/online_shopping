from django.db import models

from store.models import Product

# Create your models here.

class Cart(models.Model):
    cart_id         = models.CharField(max_length=100, blank=True)
    date_added      = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.cart_id


class CartItem(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart        = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity    = models.IntegerField()
    is_active   = models.BooleanField(default=True)

    def sub_total(self):
        return self.quantity*self.product.price

    def add_quantity(self):
        self.quantity += 1

    def reduce_quantity(self):
        self.quantity -= 1

    def __str__(self) -> str:
        return self.product.product_name