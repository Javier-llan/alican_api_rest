from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.products_mercado.api.serilizers import MercadoItemSerializer
from apps.products_mercado.models import MercadoItems
from rest_framework import viewsets

@api_view(['GET','POST'])
def product_api_view(request):
    # list
    if request.method == 'GET':
        # queryset
        queryset = MercadoItems.objects.all()
        serializer_class = MercadoItemSerializer
        return Response(serializer_class, status=status.HTTP_200_OK)
    # create
    elif request.method == 'POST':
       user_serializer = UserSerializer(data = request.data)
       # validation
       if user_serializer.is_valid():
           user_serializer.save()
           return Response({'message':'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)

       return Response(user_serializer.errors,  status = status.HTTP_400_BAD_REQUEST)
