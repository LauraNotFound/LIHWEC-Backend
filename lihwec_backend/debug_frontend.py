#!/usr/bin/env python
"""
Script de depuración para verificar los datos y diagnosticar problemas del frontend
"""

import os
import sys
import django
import json
from datetime import datetime

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lihwec_backend.settings')
django.setup()

from events.models import Category, Organization, Event
from events.serializers import EventSerializer, OrganizationSerializer, CategorySerializer

def debug_database():
    print("🔍 DEPURACIÓN DE BASE DE DATOS - FRONTEND")
    print("=" * 50)
    
    # 1. Verificar datos básicos
    print("\n📊 ESTADÍSTICAS BÁSICAS:")
    print(f"   📂 Categorías: {Category.objects.count()}")
    print(f"   🏢 Organizaciones: {Organization.objects.count()}")
    print(f"   📅 Eventos: {Event.objects.count()}")
    
    # 2. Listar todas las categorías
    print("\n📂 CATEGORÍAS DISPONIBLES:")
    categories = Category.objects.all()
    for cat in categories:
        print(f"   ID: {cat.id} | name: '{cat.name}' | display_name: '{cat.display_name}'")
    
    # 3. Listar todas las organizaciones
    print("\n🏢 ORGANIZACIONES DISPONIBLES:")
    organizations = Organization.objects.all()
    for org in organizations:
        print(f"   ID: {org.id} | name: '{org.name}'")
    
    # 4. Listar todos los eventos con detalles
    print("\n📅 EVENTOS DISPONIBLES:")
    events = Event.objects.all()
    for event in events:
        print(f"   ID: {event.id} | '{event.name}'")
        print(f"       Categoría: {event.category.name} ({event.category.display_name})")
        print(f"       Organización: {event.organization.name}")
        print(f"       Fecha: {event.date} | Modalidad: {event.modality}")
        print("   " + "-" * 40)
    
    # 5. Simular respuesta de la API /events/
    print("\n🔌 SIMULACIÓN DE API /events/:")
    try:
        events_serializer = EventSerializer(events, many=True)
        api_response = events_serializer.data
        print(f"   Cantidad de eventos serializados: {len(api_response)}")
        print(f"   Estructura del primer evento:")
        if api_response:
            first_event = api_response[0]
            for key, value in first_event.items():
                print(f"     {key}: {value}")
    except Exception as e:
        print(f"   ❌ Error al serializar: {e}")
    
    # 6. Verificar categorías específicas que busca el frontend
    print("\n🎯 VERIFICACIÓN DE CATEGORÍAS DEL FRONTEND:")
    categories_to_check = ['competencia', 'hackathon', 'evento', 'difusion']
    for cat_name in categories_to_check:
        matching_cats = Category.objects.filter(name__icontains=cat_name)
        print(f"   Categorías que contienen '{cat_name}': {matching_cats.count()}")
        for cat in matching_cats:
            print(f"     - {cat.name} ({cat.display_name})")
    
    # 7. Verificar eventos por categorías
    print("\n📊 EVENTOS POR CATEGORÍA:")
    for cat in categories:
        event_count = Event.objects.filter(category=cat).count()
        print(f"   {cat.display_name} ({cat.name}): {event_count} eventos")
    
    # 8. Crear JSON de prueba para el frontend
    print("\n📄 CREANDO ARCHIVO JSON DE PRUEBA...")
    try:
        # Serializar todos los datos
        events_data = EventSerializer(Event.objects.all(), many=True).data
        categories_data = CategorySerializer(Category.objects.all(), many=True).data
        organizations_data = OrganizationSerializer(Organization.objects.all(), many=True).data
        
        debug_data = {
            "timestamp": datetime.now().isoformat(),
            "events": events_data,
            "categories": categories_data,
            "organizations": organizations_data,
            "stats": {
                "total_events": len(events_data),
                "total_categories": len(categories_data),
                "total_organizations": len(organizations_data)
            }
        }
        
        with open('debug_api_data.json', 'w', encoding='utf-8') as f:
            json.dump(debug_data, f, indent=2, ensure_ascii=False)
        
        print("   ✅ Archivo 'debug_api_data.json' creado exitosamente")
        print("   📝 Puedes usar este archivo para probar el frontend sin el backend")
        
    except Exception as e:
        print(f"   ❌ Error al crear archivo JSON: {e}")
    
    # 9. Recomendaciones
    print("\n💡 RECOMENDACIONES:")
    
    if Event.objects.count() == 0:
        print("   ⚠️  No hay eventos. Ejecuta 'python create_admin_sample_data.py'")
    elif Event.objects.count() == 1:
        print("   ⚠️  Solo hay 1 evento. Esto puede hacer que parezca que no funciona.")
        print("       Crea más eventos usando el panel administrativo o el script de datos.")
    
    if Category.objects.count() == 0:
        print("   ⚠️  No hay categorías. El frontend necesita categorías para funcionar.")
    
    # Verificar si el puerto está bien configurado
    print("   🔧 Verifica que:")
    print("       - El servidor Django esté corriendo en http://127.0.0.1:8000")
    print("       - El config.js del frontend apunte al puerto correcto (8000, no 8080)")
    print("       - No haya errores de CORS en la consola del navegador")
    
    print("\n🚀 PRÓXIMOS PASOS:")
    print("   1. Inicia el servidor: python manage.py runserver")
    print("   2. Abre el frontend y revisa la consola del navegador (F12)")
    print("   3. Verifica que las peticiones lleguen a: http://127.0.0.1:8000/api/events/")
    print("   4. Si hay problemas, usa el panel administrativo: http://127.0.0.1:8000/api/admin-panel/")

if __name__ == "__main__":
    debug_database()
