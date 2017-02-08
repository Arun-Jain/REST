from django.shortcuts import render
from .models import Casino
from rest_framework import generics
from .serializers import CasinoSerializer
# Create your views here.

class ListCreateCasinos(generics.ListCreateAPIView):
	queryset = Casino.objects.all()
	serializer_class = CasinoSerializer
