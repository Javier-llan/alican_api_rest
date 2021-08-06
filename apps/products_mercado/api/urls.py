from django.urls import path
#from apps.products_mercado.api.api import product_api_view
#from apps.products_mercado.api.api import ProductViewSet 
from apps.products_mercado.api import views 
from rest_framework import routers

router = routers.DefaultRouter()
router.register('product', views.ProductViewSet)
urlpatterns = [
  path('api/v1/', include(router.urls)),

]