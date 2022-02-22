from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_api.serializers import ProviderSerializer
from rest_api.models import Provider

# Create your views here.
class ListProviderAPIView(ListAPIView):
    """This endpoint list all of the available providers from the database"""
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class CreateProviderAPIView(CreateAPIView):
    """This endpoint allows for creation of a provider"""
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class UpdateProviderAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific provider by passing in the id of the provider to update"""
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

class DeleteProviderAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific provider from the database"""
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer