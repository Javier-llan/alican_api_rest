from __future__ import unicode_literals
from django.http.response import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from apps.mercadoLibre.models import mercadoLibre
from apps.almacenes_japon.models import almacenes_japon
from apps.mercadoLibre.serializers import MercadoLibreSerializer
from rest_framework.response import Response
from rest_framework import generics
import json

@api_view(['GET'])
def mercado_api_view(request):

        mlibre = almacenes_japon.objects.all()
        print("all_mercado")
        print(mlibre)
        #return HttpResponse(json.simplejson.dumps(all_mercado), mimetype="application/json")
        serializer = MercadoLibreSerializer(mlibre, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def mercado_detail_view(request, pk=None):
    if request.method == 'GET':
        pkid=str(pk)
        #all_mercado = mercadoLibre.objects.filter(id=pkid).first()
        all_mercado = mercadoLibre.objects.all()
        #all_mercado.complex_filter(id=pkid).first()
        print(all_mercado)
        print(pkid)
        print(pk)
        mercado_serializers = MercadoLibreSerializer(all_mercado, many=True)
        return Response(mercado_serializers.data)
