from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from order.models import Order
from order.serializers import OrderSerializer

# Create your views here.
class ListCreatOrderAPI(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
