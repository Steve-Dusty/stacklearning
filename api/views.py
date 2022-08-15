from .models import Stack, Card
from .serializers import StackSerializer, CardSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class StackList(generics.ListCreateAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer


class StackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stack.objects.all()
    serializer_class = StackSerializer

# probably useless
class CardList(APIView):
    def get_object(self, pk):
        try:
            return Stack.objects.get(pk=pk).cards.all()
        except Stack.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        cards = self.get_object(pk)
        serializer = CardSerializer(cards, many=True)
        return Response(serializer.data)
        
class CardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    
