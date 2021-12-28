from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)
class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=2,decimal_places=2)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
