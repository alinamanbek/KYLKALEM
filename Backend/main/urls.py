'''
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

from main.views import get_latest_image_url
from . import views

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
    path('api/latest-image-url/', get_latest_image_url, name='latest_image_url'),
     path('paintings/', views.PaintingList.as_view(), name='painting-list'),

    # You can remove the line below since you don't have a HomePageView
    # path('', HomePageView.as_view(), name='home'),  
]


'''

from django.urls import path
from .views import (
    ArtistListCreateView,
    ArtistDetailView,
    ClientListCreateView,
    ClientDetailView,
    PaintingListCreateView,
    PaintingDetailView,
    BasketItemListCreateView,
    BasketItemDetailView,
    ManagerListCreateView,
    ManagerDetailView,
    MainPageListCreateView,
    MainPageDetailView
)

urlpatterns = [
    path('artists/', ArtistListCreateView.as_view(), name='artist-list'),
    path('artists/<int:pk>/', ArtistDetailView.as_view(), name='artist-detail'),
    path('clients/', ClientListCreateView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('paintings/', PaintingListCreateView.as_view(), name='painting-list'),
    path('paintings/<int:pk>/', PaintingDetailView.as_view(), name='painting-detail'),
    path('basket/', BasketItemListCreateView.as_view(), name='basket-list'),
    path('basket/<int:pk>/', BasketItemDetailView.as_view(), name='basket-detail'),
    path('managers/', ManagerListCreateView.as_view(), name='manager-list'),
    path('managers/<int:pk>/', ManagerDetailView.as_view(), name='manager-detail'),
    path('mainpage/', MainPageListCreateView.as_view(), name='mainpage-list'),
    path('mainpage/<int:pk>/', MainPageDetailView.as_view(), name='mainpage-detail'),
]
