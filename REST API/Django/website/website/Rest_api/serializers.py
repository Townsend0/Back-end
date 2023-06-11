from .models import Cafes
from rest_framework import serializers


class Serialize(serializers.ModelSerializer):
    class Meta:
        model = Cafes
        fields = '__all__'
        