'''
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
    
    
    
    
from django.http import JsonResponse
from main.models import Painting

def get_latest_image_url(request):
    try:
        # Get the latest painting
        latest_painting = Painting.objects.latest('date')
        # Construct the image URL
        image_url = request.build_absolute_uri(latest_painting.photo.url)
        return JsonResponse({'url': image_url})
    except Painting.DoesNotExist:
        return JsonResponse({'error': 'No paintings found'}, status=404)



class PaintingList(generics.ListAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

'''

from rest_framework import generics
from .models import Artist, Client, Painting, BasketItem, Manager, MainPage
from .serializers import ArtistSerializer, ClientSerializer, PaintingSerializer, BasketItemSerializer, ManagerSerializer, MainPageSerializer

class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class PaintingListCreateView(generics.ListCreateAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

class PaintingDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer

class BasketItemListCreateView(generics.ListCreateAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

class BasketItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BasketItem.objects.all()
    serializer_class = BasketItemSerializer

class ManagerListCreateView(generics.ListCreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class ManagerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

class MainPageListCreateView(generics.ListCreateAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer

class MainPageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainPage.objects.all()
    serializer_class = MainPageSerializer
