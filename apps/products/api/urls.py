from django.urls import path
from apps.products.api.api import product_api_view, find_api_view

urlpatterns = [
    path('search1/', product_api_view, name = 'product_search'),
    path('find/', find_api_view, name = 'product_find'),
    
]