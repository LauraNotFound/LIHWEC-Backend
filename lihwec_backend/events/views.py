from rest_framework import generics, filters, viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.http import JsonResponse
from .models import Event, Organization, Category, Type
from .serializers import EventSerializer, OrganizationSerializer, CategorySerializer, TypeSerializer
import logging

logger = logging.getLogger(__name__)

def index(request):
    return JsonResponse({"message": "Bienvenido a la API de LIHWEC 🚀"})

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category__name', 'modality', 'organization__name', 'type__name']
    search_fields = ['name', 'description', 'organization__name', 'location', 'type__name']

class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventSearchView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        logger.info(f"EventSearchView: Búsqueda con query='{query}'")
        
        if query:
            queryset = Event.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(organization__name__icontains=query) |
                Q(location__icontains=query) |
                Q(type__name__icontains=query)
            )
            logger.info(f"EventSearchView: Encontrados {queryset.count()} eventos")
            return queryset
        else:
            logger.info("EventSearchView: No hay query, devolviendo todos los eventos")
            return Event.objects.all()

class EventFilterView(generics.ListAPIView):
    serializer_class = EventSerializer
    
    def get_queryset(self):
        queryset = Event.objects.all()
        
        category = self.request.query_params.get('category')
        modality = self.request.query_params.get('modality')
        organization = self.request.query_params.get('organization')
        search = self.request.query_params.get('search')
        
        logger.info(f"EventFilterView: Filtros - category='{category}', modality='{modality}', organization='{organization}', search='{search}'")

        if category:
            queryset = queryset.filter(category__name__icontains=category)
            logger.info(f"EventFilterView: Filtrado por categoría, {queryset.count()} eventos")

        if modality:
            queryset = queryset.filter(modality=modality)
            logger.info(f"EventFilterView: Filtrado por modalidad, {queryset.count()} eventos")

        if organization:
            queryset = queryset.filter(organization__name__icontains=organization)
            logger.info(f"EventFilterView: Filtrado por organización, {queryset.count()} eventos")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(description__icontains=search) |
                Q(organization__name__icontains=search) |
                Q(location__icontains=search) |
                Q(type__name__icontains=search)
            )
            logger.info(f"EventFilterView: Filtrado por búsqueda, {queryset.count()} eventos")

        logger.info(f"EventFilterView: Resultado final: {queryset.count()} eventos")
        return queryset

#para las vistas de los post, update, get y delete de los modelos
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class CategoryViewSet(viewsets.ModelViewSet):  # Habilita POST/PUT/DELETE
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class OrganizationViewSet(viewsets.ModelViewSet):  # Habilita POST/PUT/DELETE
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class TypeViewSet(viewsets.ModelViewSet):  # Habilita POST/PUT/DELETE
    queryset = Type.objects.all()
    serializer_class = TypeSerializer