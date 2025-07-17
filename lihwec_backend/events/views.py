from django.shortcuts import render

from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .models import Event, Organization, Category
from .serializers import EventSerializer, OrganizationSerializer, CategorySerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__name', 'modality', 'organization__name']
    search_fields = ['name', 'description', 'organization__name', 'location', 'type']

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventSearchView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if query:
            return Event.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(organization__name__icontains=query) |
                Q(location__icontains=query) |
                Q(type__icontains=query)
            )
        return Event.objects.none()

class EventFilterView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.all()

        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__name=category)

        modality = self.request.query_params.get('modality')
        if modality:
            queryset = queryset.filter(modality=modality)

        organization = self.request.query_params.get('organization')
        if organization:
            queryset = queryset.filter(organization__name=organization)

        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(organization__name__icontains=search) |
                Q(location__icontains=search) |
                Q(type__icontains=search)
            )

        return queryset

class OrganizationListView(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer