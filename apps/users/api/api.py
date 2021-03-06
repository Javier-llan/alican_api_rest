from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.api.serializers import UserSerializer, UserListSerializer
from apps.users.models import User
from django.core.mail import send_mail
import smtplib
from alican_rest.settings import base
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string
from ..funtions import code_generator

@api_view(['GET','POST'])
def user_api_view(request):
    #users = User.objects.all().values('id', 'username', 'email', 'password', 'name', 'coderegister')
    # list
    if request.method == 'GET':
        # queryset
        users = User.objects.all().values('id', 'username', 'email', 'password', 'name', 'coderegister')
        users_serializer = UserListSerializer(users, many = True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    # create
    elif request.method == 'POST':

       user_serializer = UserSerializer(data = request.data)
       # validation
       if user_serializer.is_valid():
           user_code = code_generator()

           user_serializer.save()
           user = User.objects.filter(email=request.data['email']).first()
           user.coderegister=user_code
           user.save()

           users = User.objects.all().values('id', 'username', 'email', 'password', 'name', 'coderegister')

           #Send email
           mailServer = smtplib.SMTP(base.EMAIL_HOST, base.EMAIL_PORT)
           mailServer.starttls()
           mailServer.login(base.EMAIL_HOST_USER, base.EMAIL_HOST_PASSWORD)
           message = MIMEMultipart()
           message['From'] = base.EMAIL_HOST_USER
           message['To'] = request.data['email']
           message['Subject'] ='Bienvenida'

           content = render_to_string('welcome_email.html', {'user': request.data['name'] +" "+ request.data['last_name'],'code_register': user_code ,'frontend': base.FRONT_END_HOST+'/activate' })
           message.attach(MIMEText(content, 'html'))
           mailServer.sendmail(base.EMAIL_HOST_USER, request.data['email'], message.as_string()) 
           return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)

       return Response(user_serializer.errors,  status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def user_detail_view(request, pk = None):
    # Consulta queryset
    user = User.objects.filter(id=pk).first()
    if user:
        # retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        # update
        elif request.method == 'PUT':
            request.data
            user_serializer = UserSerializer(user, data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        # delete
        elif request.method == 'DELETE':

            user.delete()
            return Response({'message': 'Usuario Eliminado correctamente'}, status=status.HTTP_200_OK)
    return Response({'message': 'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def activate_user_view(request):
    # Consulta queryset
    user = User.objects.filter(coderegister=request.data['coderegister']).first()
    #return Response({'message': request.data['coderegister']}, status=status.HTTP_400_BAD_REQUEST)
    user_serializer = UserSerializer(user, data = request.data)
    if user :
        # retrieve
        if request.method == 'PUT':
            user.is_active=True
            user.coderegister=''
            user.save()
            return Response({'message':'Usuario acivado correctamente'}, status=200)

        return Response(user_serializer.errors,  status = status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'La clave ingresada no es correcta'}, status=status.HTTP_400_BAD_REQUEST)

