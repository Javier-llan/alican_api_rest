from django.urls import path
from apps.products.api.api import product_api_view

urlpatterns = [
    path('search1/', product_api_view, name = 'product_search'),
    
]