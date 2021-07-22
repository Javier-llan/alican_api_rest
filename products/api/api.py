from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.users.api.serializers import UserSerializer, UserListSerializer
from apps.users.models import User
from django.core.mail import send_mail
import smtplib
from alican_rest.settings import base
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string

@api_view(['POST'])
def produc_api_view(request):
    user_serializer = UserSerializer(data = request.data)
    # validation
    if user_serializer.is_valid():
        user_serializer.save()
        #Send email
        mailServer = smtplib.SMTP(base.EMAIL_HOST, base.EMAIL_PORT)
        mailServer.starttls()
        mailServer.login(base.EMAIL_HOST_USER, base.EMAIL_HOST_PASSWORD)
        message = MIMEMultipart()
        message['From'] = base.EMAIL_HOST_USER
        message['To'] = ''
        message['Subject'] ='Precio ideal'
        content = render_to_string('ideal_price_email.html', {'user': request.data['name'] +" "+ request.data['last_name'], 'frontend': base.FRONT_END_HOST+'/login' })
        message.attach(MIMEText(content, 'html'))
        mailServer.sendmail(base.EMAIL_HOST_USER, request.data['email'], message.as_string()) 
        return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors,  status = status.HTTP_400_BAD_REQUEST)
