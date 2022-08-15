from .models import Stack, Card
from rest_framework import serializers

# use nested serializers
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ['id', 'front', 'back',]

class StackSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True)

    class Meta:
        model = Stack
        fields = ['id', 'created', 'name', 'description', 'private', 'cards']

    def create(self, validated_data):
        cards_data = validated_data.pop('cards')
        print(validated_data)
        stack = Stack.objects.create(**validated_data)
        for card_data in cards_data:
            Card.objects.create(stack=stack, **card_data)
        return stack
    
