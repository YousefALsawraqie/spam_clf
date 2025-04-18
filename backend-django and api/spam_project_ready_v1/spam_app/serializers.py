from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from .models import ClassifiedMessage
from rest_framework import serializers


class StuSerializer(ModelSerializer):
    class Meta:
        model = ClassifiedMessage
        fields = '__all__'