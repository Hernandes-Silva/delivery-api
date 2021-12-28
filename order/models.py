from django.db import models

from products.models import Product

# Create your models here.
class Order(models.Model):
    product = models.ForeignKey(Product, related_name='orders', on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)