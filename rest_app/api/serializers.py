from rest_app.models import Casino
from rest_framework import serializers

class CasinoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Casino
		fields = ("id", "name", "address")

#class CreateCasinoSerializer(serializers.ModelSerializer):
#	class Meta:
#		model = Casino
#		fields = ("name", "address")
