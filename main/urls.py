"""main URL Configuration

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
from core.api import viewsets as coreviewset
# from users.api import viewsets as userviewset
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from users.api import viewsets as userviewset

route = routers.DefaultRouter()

# route.register(r'users', userviewset.UserViewSet)

route.register(r'clients', coreviewset.ClientViewSet, basename='Clients')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', userviewset.MyObtainTokenPairView.as_view()),
    path('register/', userviewset.RegisterView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('token/verify', TokenVerifyView.as_view()),
    path('', include(route.urls))
]
