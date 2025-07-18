from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json
from .models import Event, Organization, Category
from .serializers import EventSerializer, OrganizationSerializer, CategorySerializer

class AdminPanelView(View):
    def get(self, request):
        """Vista principal del panel administrativo"""
        events = Event.objects.all().order_by('-id')[:10]  # Últimos 10 eventos
        organizations = Organization.objects.all()
        categories = Category.objects.all()
        
        context = {
            'events': events,
            'organizations': organizations,
            'categories': categories,
            'events_count': Event.objects.count(),
            'organizations_count': organizations.count(),
            'categories_count': categories.count(),
        }
        return render(request, 'events/admin_panel.html', context)

class EventManagementView(View):
    def get(self, request):
        """Vista de gestión de eventos"""
        events = Event.objects.all().order_by('-id')
        organizations = Organization.objects.all()
        categories = Category.objects.all()
        
        context = {
            'events': events,
            'organizations': organizations,
            'categories': categories,
        }
        return render(request, 'events/event_management.html', context)

class OrganizationManagementView(View):
    def get(self, request):
        """Vista de gestión de organizaciones"""
        organizations = Organization.objects.all().order_by('-id')
        context = {'organizations': organizations}
        return render(request, 'events/organization_management.html', context)

class CategoryManagementView(View):
    def get(self, request):
        """Vista de gestión de categorías"""
        categories = Category.objects.all().order_by('-id')
        context = {'categories': categories}
        return render(request, 'events/category_management.html', context)

# API Views para el panel administrativo
@method_decorator(csrf_exempt, name='dispatch')
class AdminEventAPIView(View):
    def post(self, request):
        """Crear evento"""
        try:
            data = json.loads(request.body)
            serializer = EventSerializer(data=data)
            if serializer.is_valid():
                event = serializer.save()
                return JsonResponse({
                    'success': True, 
                    'message': 'Evento creado exitosamente',
                    'event': EventSerializer(event).data
                })
            return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    def put(self, request, event_id):
        """Actualizar evento"""
        try:
            event = get_object_or_404(Event, id=event_id)
            data = json.loads(request.body)
            serializer = EventSerializer(event, data=data)
            if serializer.is_valid():
                event = serializer.save()
                return JsonResponse({
                    'success': True, 
                    'message': 'Evento actualizado exitosamente',
                    'event': EventSerializer(event).data
                })
            return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    def delete(self, request, event_id):
        """Eliminar evento"""
        try:
            event = get_object_or_404(Event, id=event_id)
            event_name = event.name
            event.delete()
            return JsonResponse({
                'success': True, 
                'message': f'Evento "{event_name}" eliminado exitosamente'
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class AdminOrganizationAPIView(View):
    def post(self, request):
        """Crear organización"""
        try:
            data = json.loads(request.body)
            serializer = OrganizationSerializer(data=data)
            if serializer.is_valid():
                organization = serializer.save()
                return JsonResponse({
                    'success': True, 
                    'message': 'Organización creada exitosamente',
                    'organization': OrganizationSerializer(organization).data
                })
            return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    def put(self, request, org_id):
        """Actualizar organización"""
        try:
            organization = get_object_or_404(Organization, id=org_id)
            data = json.loads(request.body)
            serializer = OrganizationSerializer(organization, data=data)
            if serializer.is_valid():
                organization = serializer.save()
                return JsonResponse({
                    'success': True, 
                    'message': 'Organización actualizada exitosamente',
                    'organization': OrganizationSerializer(organization).data
                })
            return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    def delete(self, request, org_id):
        """Eliminar organización"""
        try:
            organization = get_object_or_404(Organization, id=org_id)
            org_name = organization.name
            organization.delete()
            return JsonResponse({
                'success': True, 
                'message': f'Organización "{org_name}" eliminada exitosamente'
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)

@method_decorator(csrf_exempt, name='dispatch')
class AdminCategoryAPIView(View):
    def post(self, request):
        """Crear categoría"""
        try:
            data = json.loads(request.body)
            serializer = CategorySerializer(data=data)
            if serializer.is_valid():
                category = serializer.save()
                return JsonResponse({
                    'success': True, 
                    'message': 'Categoría creada exitosamente',
                    'category': CategorySerializer(category).data
                })
            return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    def put(self, request, cat_id):
        """Actualizar categoría"""
        try:
            category = get_object_or_404(Category, id=cat_id)
            data = json.loads(request.body)
            serializer = CategorySerializer(category, data=data)
            if serializer.is_valid():
                category = serializer.save()
                return JsonResponse({
                    'success': True, 
                    'message': 'Categoría actualizada exitosamente',
                    'category': CategorySerializer(category).data
                })
            return JsonResponse({'success': False, 'errors': serializer.errors}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
    
    def delete(self, request, cat_id):
        """Eliminar categoría"""
        try:
            category = get_object_or_404(Category, id=cat_id)
            cat_name = category.name
            category.delete()
            return JsonResponse({
                'success': True, 
                'message': f'Categoría "{cat_name}" eliminada exitosamente'
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
