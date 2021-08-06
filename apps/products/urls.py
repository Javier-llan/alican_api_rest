from django.urls import path
from apps.products.views import ProductList, ProductDetail

urlpatterns = [
    path('', ProductList.as_view()),
    path('<int:pk>', ProductDetail.as_view())
]