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
import json
from django.http import HttpResponse

@api_view(['GET','POST'])
def product_api_view(request):
    
    if request.method == 'POST':
        # queryset
        param=request.data['params']
        productss = Products.objects.filter(titulo__contains=param).values('titulo', 'descripcion', 'precio', 'imagen')
        products = mercadoLibre.objects.filter(id="432121700").values('id','titulo', 'descripcion', 'precio', 'imagen')
        #products = Products.objects.all().values('titulo', 'descripcion', 'precio', 'imagen')

        products_serializer = ProductListSerializer(products, many = True)
        #return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(products_serializer.data, status=status.HTTP_200_OK)
        #return HttpResponse(json.dumps(products_serializer),content_type="application/json")
