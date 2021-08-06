from rest_framework import serializers
from apps.products_mercado.models import MercadoItems

class MercadoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MercadoItems
        fields = {'titulo','descripcion','precio'}