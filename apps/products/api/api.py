from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.products.api.serializers import ProductListSerializer, ProductSerializer
from apps.products.models import Products
from apps.mercadoLibre.models import mercadoLibre
from django.core.mail import send_mail
import smtplib
from alican_rest.settings import base
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from itertools import chain
from apps.almacenes_japon.models import almacenes_japon
from apps.point.models import point
#refri
from apps.comandato.models import comandato
from apps.mercadoLibre.serializers import MercadoLibreSerializer

@api_view(['GET','POST'])
def product_api_view(request):
    
    if request.method == 'POST':
        # queryset
        param=request.data['params']
        mlibre = mercadoLibre.objects.filter(titulo__contains=param)
        ajapon = almacenes_japon.objects.filter(titulo__contains=param)
        cmdt = comandato.objects.filter(titulo__contains=param)
        pnt = point.objects.filter(titulo__contains=param)
        result_list = list(chain(mlibre, ajapon, pnt, cmdt))
        #products = Products.objects.all().values('titulo', 'descripcion', 'precio', 'imagen')

        products_serializer = MercadoLibreSerializer(result_list, many = True)
        #return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(products_serializer.data, status=status.HTTP_200_OK)
        #return HttpResponse(json.dumps(products_serializer),content_type="application/json")

@api_view(['GET','POST'])
def find_api_view(request):
    
    if request.method == 'POST':
        # queryset
        param=request.data['id']
        mlibre = mercadoLibre.objects.filter(codigo=param).first()
        print(mlibre)
        if(mlibre):
            data=mlibre
        else:
            ajapon = almacenes_japon.objects.filter(codigo=param).first()
            if(ajapon):
                data = ajapon
            else:
                cmdt = comandato.objects.filter(codigo=param).first()
                if(cmdt):
                    data=cmdt
                else:
                    pnt = point.objects.filter(codigo=param).first()
                    data=pnt

        products_serializer = MercadoLibreSerializer(data, many = True)
        #return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(products_serializer.data, status=status.HTTP_200_OK)
        #return HttpResponse(json.dumps(products_serializer),content_type="application/json")
