from django.http.response import Http404
from rest_framework.response import Response
from core import models
from rest_framework import viewsets
from core.api import serializers
from rest_framework.permissions import IsAuthenticated

class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.ClientSerializer
    queryset = models.Client.objects.all()

    def create(self,request, *args, **kwargs ):
        client_data = request.data

        new_address = models.Address.objects.create(**client_data['address'])
        new_address.save()
        client = models.Client.objects.create(name=client_data['name'], phone=client_data['phone'], address=new_address)
        client.save()
        serializer = serializers.ClientSerializer(client)
        
        return Response(serializer.data)

    def update(self,request, pk):
        data = request.data
        try:
            client_object = models.Client.objects.get(id=pk)
        except models.Client.DoesNotExist:
            raise Http404

        address_data = data['address']
        address_object = models.Address.objects.get(id=address_data['id'])
        address_object.address = address_data["address"] or address_object.address
        address_object.number = address_data["number"] or address_object.number
        address_object.city = address_data["city"] or address_object.city
        address_object.state = address_data["state"] or address_object.state
        address_object.country = address_data["country"] or address_object.country
        address_object.zipCode = address_data["zipCode"] or address_object.zipCode
        address_object.save()

        client_object.name = data["name"] or client_object.name
        client_object.phone = data["phone"] or client_object.phone
        client_object.address = address_object


        client_object.save()

        serializer = serializers.ClientSerializer(client_object)
        
        return Response(serializer.data)
    