from rest_framework import serializers
from .models import City

class CitySerializer(serializers.ModelSerializer):
    city = serializers.CharField()
    class Meta:
        model = City
        fields = '__all__'