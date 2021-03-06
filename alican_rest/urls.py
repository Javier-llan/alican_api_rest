"""alican_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

from apps.users.views import Login
from apps.users.views import Logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario/', include('apps.users.api.urls')),
    path('products/', include('apps.products.api.urls')),
    path('logout/', Logout.as_view(), name='logout'),
    path('',Login.as_view(),name='login'),
    path('product/', include('apps.products.urls')),
    path('mercadolibre/', include('apps.mercadoLibre.urls')),
    path('like/', include('apps.like.api.urls'))
]
