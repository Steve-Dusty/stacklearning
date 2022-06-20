from .models import Stack, Card
from rest_framework import serializers

class StackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stack
        fields = ['created', 'name']

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['front', 'back', 'stack']