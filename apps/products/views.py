from rest_framework import generics
from apps.products.models import Products
from apps.products.serializers import ProductSerializer

class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer