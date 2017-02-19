from django.shortcuts import render
from rest_app.models import Casino
from rest_framework import generics
from .serializers import CasinoSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.decorators import throttle_classes
import django_filters
# Create your views here.

@permission_classes((AllowAny, ))
class ListCreateCasinos(generics.ListCreateAPIView):
	queryset = Casino.objects.all()
	serializer_class = CasinoSerializer

class DetailAPIView(generics.RetrieveAPIView):
	queryset = Casino.objects.all()
	serializer_class = CasinoSerializer

	@throttle_classes([UserRateThrottle])
	def example_view(request, format=None):
		content = {
		'status': 'request was permitted'
		}
		return Response(content)
