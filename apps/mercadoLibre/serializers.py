from rest_framework import serializers
from apps.mercadoLibre.models import mercadoLibre

class MercadoLibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = mercadoLibre
        fields =('id', 'codigo', 'tienda', 'titulo', 'descripcion', 'precio', 'imagen','link', 'fecha')