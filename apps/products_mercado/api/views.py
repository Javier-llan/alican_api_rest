from apps.products_mercado.api.serilizers import MercadoItemSerializer
from apps.products_mercado.models import MercadoItems
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
  queryset = MercadoItems.objects.all()
  serializer_class = MercadoItemSerializer