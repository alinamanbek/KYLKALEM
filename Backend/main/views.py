from rest_framework import generics
from .models import Artist, Client, Painting, BasketItem
from .serializers import ArtistSerializer, ClientSerializer, PaintingSerializer, BasketItemSerializer

class ArtistListCreateAPIView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ClientListCreateAPIView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class PaintingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

class PaintingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

class BasketItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

class BasketItemRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer
