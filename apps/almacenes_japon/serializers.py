from rest_framework import serializers
from apps.almacenes_japon.models import almacenes_japon

class AlmacenesJaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = almacenes_japon
        fields =('id', 'codigo', 'tienda', 'titulo', 'descripcion', 'precio', 'imagen','link', 'fecha')