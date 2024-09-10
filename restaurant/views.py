# Create your views here.
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Restaurant, Category, Item
from .serializers import RestaurantSerializer, CategorySerializer, ItemSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwnerOrEmployee
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    # permission_classes = [AllowAny]
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]

    # Add the search and filter backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # Define the fields to filter by
    filterset_fields = ['location']
    # Define the fields to search by
    search_fields = ['name', 'location']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrEmployee]
    # Add the filter and search backends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    # Define the fields to filter by
    filterset_fields = ['restaurant', 'category', 'price']
    # Include restaurant and category in the search fields
    search_fields = ['name', 'description', 'restaurant__name', 'category__name']
