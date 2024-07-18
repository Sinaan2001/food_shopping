from django.db import models
from shop.models import *


# Create your models here.
class cartlist(models.Model):
    def __str__(self):
        return self.cart_id

    cart_id=models.CharField(max_length=250,unique=True)
    date_added=models.DateTimeField(auto_now_add=True)

class items(models.Model):
    def __str__(self):
        return self.product.name
    product=models.ForeignKey(products,on_delete=models.CASCADE)
    cart=models.ForeignKey(cartlist,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    active=models.BooleanField(default=True)

    def total(self):
        return self.product.price*self.quantity

