#!/usr/bin/env python
"""
Script de solución rápida para problemas del frontend
"""

import os
import sys
import django
from datetime import datetime, timedelta

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lihwec_backend.settings')
django.setup()

from events.models import Category, Organization, Event

def fix_frontend_issues():
    print("🔧 SOLUCIONANDO PROBLEMAS DEL FRONTEND")
    print("=" * 50)
    
    # 1. Verificar y crear categorías básicas si no existen
    print("\n📂 Verificando categorías...")
    basic_categories = [
        {"name": "tecnologia", "display_name": "Tecnología"},
        {"name": "educacion", "display_name": "Educación"},
        {"name": "general", "display_name": "General"},
    ]
    
    for cat_data in basic_categories:
        category, created = Category.objects.get_or_create(
            name=cat_data["name"],
            defaults={"display_name": cat_data["display_name"]}
        )
        if created:
            print(f"   ✅ Categoría creada: {category.display_name}")
        else:
            print(f"   ℹ️  Categoría existente: {category.display_name}")
    
    # 2. Verificar y crear organizaciones básicas si no existen
    print("\n🏢 Verificando organizaciones...")
    basic_orgs = [
        {"name": "Universidad Nacional", "description": "Institución educativa"},
        {"name": "TechHub", "description": "Comunidad tecnológica"},
        {"name": "Organización General", "description": "Organización general"},
    ]
    
    for org_data in basic_orgs:
        organization, created = Organization.objects.get_or_create(
            name=org_data["name"],
            defaults={"description": org_data["description"]}
        )
        if created:
            print(f"   ✅ Organización creada: {organization.name}")
        else:
            print(f"   ℹ️  Organización existente: {organization.name}")
    
    # 3. Crear eventos de prueba si hay pocos
    print(f"\n📅 Verificando eventos... (actuales: {Event.objects.count()})")
    
    if Event.objects.count() < 3:
        print("   ⚠️  Pocos eventos detectados. Creando eventos de prueba...")
        
        # Obtener categorías y organizaciones
        tech_cat = Category.objects.filter(name="tecnologia").first()
        edu_cat = Category.objects.filter(name="educacion").first()
        general_cat = Category.objects.filter(name="general").first()
        
        uni_org = Organization.objects.filter(name__icontains="Universidad").first()
        tech_org = Organization.objects.filter(name__icontains="Tech").first()
        general_org = Organization.objects.filter(name__icontains="General").first()
        
        # Crear eventos de prueba
        test_events = [
            {
                "name": "Workshop de Python",
                "date": datetime.now().date() + timedelta(days=7),
                "time": "14:00:00",
                "modality": "presencial",
                "location": "Auditorio Principal",
                "organization": tech_org or Organization.objects.first(),
                "category": tech_cat or Category.objects.first(),
                "type": "difusor",
                "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c",
                "description": "Aprende Python desde cero en este workshop práctico.",
                "link": "https://ejemplo.com/workshop-python"
            },
            {
                "name": "Conferencia de IA",
                "date": datetime.now().date() + timedelta(days=15),
                "time": "09:00:00",
                "modality": "virtual",
                "location": "Plataforma Zoom",
                "organization": uni_org or Organization.objects.first(),
                "category": tech_cat or Category.objects.first(),
                "type": "difusor",
                "image": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e",
                "description": "Conferencia sobre inteligencia artificial y machine learning.",
                "link": "https://ejemplo.com/conferencia-ia"
            },
            {
                "name": "Seminario de Educación Digital",
                "date": datetime.now().date() + timedelta(days=20),
                "time": "16:00:00",
                "modality": "hibrido",
                "location": "Campus Universitario",
                "organization": uni_org or Organization.objects.first(),
                "category": edu_cat or Category.objects.first(),
                "type": "difusor",
                "image": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f",
                "description": "Seminario sobre herramientas digitales en la educación.",
                "link": "https://ejemplo.com/seminario-educacion"
            },
            {
                "name": "Hackathon Nacional 2025",
                "date": datetime.now().date() + timedelta(days=30),
                "time": "08:00:00",
                "modality": "presencial",
                "location": "Centro de Convenciones",
                "organization": tech_org or Organization.objects.first(),
                "category": tech_cat or Category.objects.first(),
                "type": "competencia",
                "image": "https://images.unsplash.com/photo-1540575467063-178a50c2df87",
                "description": "Hackathon nacional para desarrolladores y diseñadores.",
                "link": "https://ejemplo.com/hackathon-2025"
            },
            {
                "name": "Mesa Redonda: Futuro de la Tecnología",
                "date": datetime.now().date() + timedelta(days=45),
                "time": "10:00:00",
                "modality": "virtual",
                "location": "Microsoft Teams",
                "organization": general_org or Organization.objects.first(),
                "category": general_cat or Category.objects.first(),
                "type": "difusor",
                "image": "https://images.unsplash.com/photo-1515187029135-18ee286d815b",
                "description": "Mesa redonda con expertos sobre el futuro de la tecnología.",
                "link": "https://ejemplo.com/mesa-redonda"
            }
        ]
        
        for event_data in test_events:
            event, created = Event.objects.get_or_create(
                name=event_data["name"],
                defaults=event_data
            )
            if created:
                print(f"   ✅ Evento creado: {event.name}")
            else:
                print(f"   ℹ️  Evento existente: {event.name}")
    
    # 4. Mostrar resumen final
    print(f"\n📊 RESUMEN FINAL:")
    print(f"   📂 Categorías: {Category.objects.count()}")
    print(f"   🏢 Organizaciones: {Organization.objects.count()}")
    print(f"   📅 Eventos: {Event.objects.count()}")
    
    # 5. Verificar que todos los eventos tengan referencias válidas
    print(f"\n✅ VERIFICACIÓN DE INTEGRIDAD:")
    events_with_issues = 0
    for event in Event.objects.all():
        try:
            # Intentar acceder a todos los campos relacionados
            org_name = event.organization.name
            cat_name = event.category.name
        except Exception as e:
            print(f"   ❌ Problema con evento '{event.name}': {e}")
            events_with_issues += 1
    
    if events_with_issues == 0:
        print("   ✅ Todos los eventos tienen referencias válidas")
    else:
        print(f"   ❌ {events_with_issues} eventos tienen problemas")
    
    print(f"\n🚀 LISTO PARA PROBAR:")
    print("   1. Inicia el servidor: python manage.py runserver")
    print("   2. Abre el frontend en tu navegador")
    print("   3. Deberías ver los eventos en ambas secciones")
    print("   4. Si no funciona, revisa la consola del navegador (F12)")

if __name__ == "__main__":
    fix_frontend_issues()
