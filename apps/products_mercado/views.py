from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.products_mercado.models import MercadoItems
from apps.products_mercado.api.serilizers import MercadoItemSerializer

class ProductosApiView(APIView):

    def get(self, request):
        all_products = MercadoItems.objects.all()
        serializer = MercadoItemSerializer(all_products, many=True)
        return Response(serializer.data)

