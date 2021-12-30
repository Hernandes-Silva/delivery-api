
from django.db.models.fields import CharField
from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.decorators import api_view
from django.db.models import Count
from rest_framework.response import Response
from django.db.models.functions import TruncDate, Cast
# Create your views here.
@api_view(['GET',])
def best_selling_products(request):
    orders = Order.objects.all().filter(paid=True)
    best_selling = orders.values('product', 'product__name').annotate(value=Count('product'))\
        .order_by('-value')
    return Response(best_selling[:5])
@api_view(['GET',])
def years_orders(request):
    orders = Order.objects.all().filter(paid=True)
    orders = orders.annotate(date=Cast(TruncDate('created'), CharField()))\
    .order_by('date').values('date').annotate(value=Count('date'))
    return Response(orders)
    
class ListCreatOrderAPI(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
