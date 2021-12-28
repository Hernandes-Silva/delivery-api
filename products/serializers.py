from django.db.models import fields
from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    model = Category
    fields = '__all__'
class ProductSerializer(serializers.ModelSerializer):
    model = Product
    fields = '__all__'