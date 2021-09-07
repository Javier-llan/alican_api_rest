from rest_framework import generics, mixins, status, viewsets
from apps.products.models import Products
from apps.products.serializers import ProductSerializer
from rest_framework.response import Response
# Permissions
from rest_framework.permissions import IsAuthenticated


class ProductList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductSearch(generics.ListAPIView):
    
    queryset = Products.objects.filter(titulo="Macbook Pro Retina Core I7 16gb Ram 15 256gb 500gb Solido")
    serializer_class = ProductSerializer     