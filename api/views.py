from .models import Stack, Card
from .serializers import StackSerializer, CardSerializer
from rest_framework import generics

class StackList(generics.ListCreateAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class StackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer
    
class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    
