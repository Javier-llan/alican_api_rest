from django.views import View
from .models import Product
from django.http import JsonResponse
# Create your views here.
class ProductListView(View):
    def get(self, request):
        queryset  = Product.objects.all()
        #return list return JsonResponse({"models_to_return": list(queryset)})
        return JsonResponse({"models_to_return": list(queryset)})
