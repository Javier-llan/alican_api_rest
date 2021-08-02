from rest_framework_mongoengine import serializers
from apps.products_mercado.models import MercadoItems

class MercadoItemSerializer(serializers.DocumentSerializer):
    class Meta:
        model = MercadoItems
        fields = {'titulo','descripcion','precio'}