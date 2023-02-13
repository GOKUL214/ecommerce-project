from django.db import models
from shop.models import Product

# Create your models here.
class Cart(models.Model):
    cart_id=models.CharField(max_length=250, blank=True)
    data_added=models.DateField(auto_now_add=True)

    class Meta:
        db_table='cart'
        ordering=['data_added']
    def __str__(self):
        return '{}'.format(self.cart_id)

class Cartitem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    class Meta:
        db_table='cartitem'
    def SubTotal(self):
        return self.product.price * self.quantity
    def __str__(self):
        return '{}'.format(self.product)

