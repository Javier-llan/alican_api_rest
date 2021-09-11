from __future__ import unicode_literals
from django.http.response import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from apps.mercadoLibre.models import mercadoLibre
from apps.almacenes_japon.models import almacenes_japon
from apps.point.models import point
#refri
from apps.comandato.models import comandato
from apps.mercadoLibre.serializers import MercadoLibreSerializer
from apps.almacenes_japon.serializers import AlmacenesJaponSerializer
from rest_framework.response import Response
from rest_framework import generics
from itertools import chain

@api_view(['GET'])
def mercado_api_view(request):

        mlibre = mercadoLibre.objects.all()
        ajapon = almacenes_japon.objects.all()
        cmdt = comandato.objects.all()
        pnt = cmdt = point.objects.all()
        print("all_mercado")
        print(mlibre)
        
        result_list = list(chain(mlibre, ajapon, cmdt, pnt))
        #return HttpResponse(json.simplejson.dumps(all_mercado), mimetype="application/json")
        serializer = MercadoLibreSerializer(result_list, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def mercado_detail_view(request, pk=None):
    if request.method == 'GET':
        pkid=str(pk)
        #all_mercado = mercadoLibre.objects.filter(id=pkid).first()
        all_mercado = mercadoLibre.objects.filter(codigo=pkid)
        if(all_mercado.count()==0):
            all_mercado = almacenes_japon.objects.filter(codigo=pkid)
        if(all_mercado.count()==0):
            all_mercado = point.objects.filter(codigo=pkid)
        if(all_mercado.count()==0):
            all_mercado = comandato.objects.filter(codigo=pkid)        

        print(all_mercado.count())
        print(pkid)
        print(pk)
        mercado_serializers = MercadoLibreSerializer(all_mercado, many=True)
        return Response(mercado_serializers.data)
