from rest_framework import serializers
from apps.products.models import Products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('titulo', 'tienda', 'descripcion', 'precio', 'imagen')


class ProductListSerializer(serializers.Serializer):
    class Meta:
        model = Products

    def to_representation(self, instance):
        return {
            'titulo': instance['titulo'],
            'descripcion': instance['descripcion'],
            'tienda': instance['tienda'],
            'precio': instance['precio'],
            'imagen': instance['imagen']
        }
