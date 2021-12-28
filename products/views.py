from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from products.serializers import CategorySerializer, ProductSerializer
from products.models import Category, Product
# Create your views here.

class ListCreateCategoryAPI(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class ListCreateProductAPI(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
