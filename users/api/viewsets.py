from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .serializers import MyTokenObtainPairSerializer, RegisterSerializer


@extend_schema(summary='Obter par de tokens JWT', tags=['Auth'])
class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


@extend_schema(summary='Renovar access token', tags=['Auth'])
class TokenRefreshViewDoc(TokenRefreshView):
    pass


@extend_schema(summary='Verificar validade do token', tags=['Auth'])
class TokenVerifyViewDoc(TokenVerifyView):
    pass


@extend_schema(summary='Registrar novo usuário', tags=['Auth'])
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer