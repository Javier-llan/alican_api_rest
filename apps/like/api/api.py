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
from apps.like.api.serializers import LikeSerializer
from apps.like.models import like

@api_view(['GET','POST'])
def like_add_api_view(request):
    
    if request.method == 'POST':
        # queryset
        user=request.data['id_user']
        product=request.data['id_product']
        newlike = like()
        newlike.id_user=user
        newlike.id_product=product
        newlike.save()
        return Response({"status":True}, status=status.HTTP_200_OK)


@api_view(['GET','POST'])
def like_user_api_view(request):
    
    if request.method == 'POST':
        # queryset
        param=request.data['id_user']
        likes = like.objects.filter(id_user=param)
        likes_serializer = LikeSerializer(likes, many = True)
        
        return Response(likes_serializer.data, status=status.HTTP_200_OK)
