from django.urls import path
from .views import (
    ArtistListCreateAPIView,
    ArtistRetrieveUpdateDestroyAPIView,
    ClientListCreateAPIView,
    ClientRetrieveUpdateDestroyAPIView,
    PaintingListCreateAPIView,
    PaintingRetrieveUpdateDestroyAPIView,
    BasketItemListCreateAPIView,
    BasketItemRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # Include the API URLs directly here
    path('artists/', ArtistListCreateAPIView.as_view(), name='artist-list-create'),
    path('artists/<int:pk>/', ArtistRetrieveUpdateDestroyAPIView.as_view(), name='artist-retrieve-update-destroy'),
    path('clients/', ClientListCreateAPIView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyAPIView.as_view(), name='client-retrieve-update-destroy'),
    path('paintings/', PaintingListCreateAPIView.as_view(), name='painting-list-create'),
    path('paintings/<int:pk>/', PaintingRetrieveUpdateDestroyAPIView.as_view(), name='painting-retrieve-update-destroy'),
    path('basket/', BasketItemListCreateAPIView.as_view(), name='basket-item-list-create'),
    path('basket/<int:pk>/', BasketItemRetrieveUpdateDestroyAPIView.as_view(), name='basket-item-retrieve-update-destroy'),
    # You can remove the line below since you don't have a HomePageView
    # path('', HomePageView.as_view(), name='home'),  
]
