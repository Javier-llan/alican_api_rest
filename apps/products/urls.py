from django.urls import path
from apps.products.views import ProductList, ProductDetail, ProductSearch
from django.conf.urls import include, url  
from rest_framework import routers

#router = routers.SimpleRouter()
#router.register(r'', ProductList.as_view()
#router.register(r'find', ProductDetail.as_view())
#router.register(r'searchsearch', ProductSearch)

urlpatterns = [
    path('', ProductList.as_view()),
    path('search', ProductSearch.as_view()),
    path('<int:pk>', ProductDetail.as_view())
]

#urlpatterns = [
#   url(r'^', include(router.urls)),
#]