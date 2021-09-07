from __future__ import unicode_literals
from rest_framework.decorators import api_view
from apps.mercadoLibre.models import mercadoLibre
from apps.mercadoLibre.serializers import MercadoLibreSerializer
from rest_framework.response import Response

@api_view(['GET'])
def mercado_api_view(request):
        all_mercado = mercadoLibre.objects.all()
        serializer = MercadoLibreSerializer(all_mercado, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def mercado_detail_view(request, pk=None):
    if request.method == 'GET':
        all_mercado = mercadoLibre.objects.filter(id=pk).first()
        print(pk)
        mercado_serializers = MercadoLibreSerializer(all_mercado)
        return Response(mercado_serializers.data)
