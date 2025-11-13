from django.db.models import fields
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import action
from core import models

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = '__all__'
    address = AddressSerializer(many=False)
