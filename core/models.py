from django.db import models
from uuid import uuid4

# Create your models here.

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    address = models.CharField(max_length=200)
    number = models.IntegerField()
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zipCode = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    address = models.ForeignKey(Address, related_name='client', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)