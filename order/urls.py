from django.urls import path
from order import views
urlpatterns = [
    path('api/order/', views.ListCreatOrderAPI.as_view(), name="order_api"),
    path('api/order/best-selling/', views.best_selling_products, name="best_selling-api"), 
]