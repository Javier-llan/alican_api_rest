from django.urls import path
from apps.like.api.api import like_add_api_view, like_user_api_view

urlpatterns = [
    path('add/', like_add_api_view, name = 'like_add'),
    path('get_by_user/', like_user_api_view, name = 'like_user'),
    
]