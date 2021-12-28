from django.urls import path
from order import views
urlpatterns = [
    path('api/order/', views.ListCreatOrderAPI.as_view(), name="order_api"),
    
]