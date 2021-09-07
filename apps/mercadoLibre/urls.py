from django.urls import path
from apps.mercadoLibre.views import mercado_api_view, mercado_detail_view

urlpatterns = [
    path('mercadolibre/', mercado_api_view, name ='mercado_list'),
    path('mercadolibre/<int:pk>/', mercado_detail_view, name='mercado_detail')
]