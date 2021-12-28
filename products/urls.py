from django.urls import path
from products import views
urlpatterns = [
    path('api/products/', views.ListCreateProductAPI.as_view(), name="product_api"),
    path('api/category/', views.ListCreateCategoryAPI.as_view(), name='category_api')
]