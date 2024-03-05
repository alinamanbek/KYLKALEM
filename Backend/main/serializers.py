'''
from rest_framework import serializers
from .models import Artist, Client, Painting, BasketItem

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = '__all__'

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = '__all__'




from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Painting
from .serializers import PaintingSerializer

class PaintingView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        paintings = Painting.objects.all()
        serializer = PaintingSerializer(paintings, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        painting_serializer = PaintingSerializer(data=request.data)
        if painting_serializer.is_valid():
            painting_serializer.save()
            return Response(painting_serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('error', painting_serializer.errors)
            return Response(painting_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''
from rest_framework import serializers
from .models import Artist, Client, Painting, BasketItem, Manager, MainPage

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class PaintingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Painting
        fields = '__all__'

class BasketItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketItem
        fields = '__all__'

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = '__all__'

class MainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPage
        fields = '__all__'
