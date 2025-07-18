#!/usr/bin/env python
"""
Script para verificar y mostrar los datos actuales en la base de datos
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lihwec_backend.settings')
django.setup()

from events.models import Category, Organization, Event

def check_database_status():
    print("🔍 Verificando estado actual de la base de datos...\n")
    
    # Verificar categorías
    print("📂 CATEGORÍAS:")
    categories = Category.objects.all()
    if categories:
        for cat in categories:
            event_count = cat.event_set.count()
            print(f"   ID: {cat.id} | Nombre: {cat.name} | Display: {cat.display_name} | Eventos: {event_count}")
    else:
        print("   ❌ No hay categorías en la base de datos")
    
    print(f"\n   Total de categorías: {categories.count()}")
    
    # Verificar organizaciones
    print("\n🏢 ORGANIZACIONES:")
    organizations = Organization.objects.all()
    if organizations:
        for org in organizations:
            event_count = org.event_set.count()
            print(f"   ID: {org.id} | Nombre: {org.name} | Eventos: {event_count}")
    else:
        print("   ❌ No hay organizaciones en la base de datos")
    
    print(f"\n   Total de organizaciones: {organizations.count()}")
    
    # Verificar eventos
    print("\n📅 EVENTOS:")
    events = Event.objects.all()
    if events:
        for event in events:
            print(f"   ID: {event.id} | Nombre: {event.name}")
            print(f"       Organización: {event.organization.name}")
            print(f"       Categoría: {event.category.name} ({event.category.display_name})")
            print(f"       Fecha: {event.date} | Modalidad: {event.modality}")
            print("   " + "-" * 50)
    else:
        print("   ❌ No hay eventos en la base de datos")
    
    print(f"\n   Total de eventos: {events.count()}")
    
    # Verificar posibles problemas
    print("\n🔍 DIAGNÓSTICO:")
    
    # Verificar eventos sin organización o categoría válida
    orphaned_events = []
    for event in events:
        try:
            # Intentar acceder a la organización y categoría
            org_name = event.organization.name
            cat_name = event.category.name
        except:
            orphaned_events.append(event)
    
    if orphaned_events:
        print("   ⚠️  Eventos con referencias rotas encontrados:")
        for event in orphaned_events:
            print(f"      - {event.name} (ID: {event.id})")
    else:
        print("   ✅ Todas las referencias de eventos están correctas")
    
    # Verificar si hay suficientes datos para el frontend
    if events.count() == 0:
        print("   ❌ PROBLEMA: No hay eventos para mostrar en el frontend")
    elif events.count() == 1:
        print("   ⚠️  ADVERTENCIA: Solo hay 1 evento, puede parecer que no funciona")
    else:
        print(f"   ✅ Hay {events.count()} eventos disponibles para el frontend")

if __name__ == "__main__":
    check_database_status()
