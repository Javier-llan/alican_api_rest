from rest_framework import serializers
from apps.mercadoLibre.models import mercadoLibre

class MercadoLibreSerializer(serializers.ModelSerializer):
    class Meta:
        model = mercadoLibre
        fields =('id', 'titulo', 'descripcion', 'precio', 'imagen','link', 'fecha')