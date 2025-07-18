#!/usr/bin/env python
"""
Script para crear datos de prueba para el panel administrativo de LIHWEC
Ejecutar desde el directorio del proyecto Django
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

def create_sample_data():
    print("🚀 Creando datos de prueba para el panel administrativo...")
    
    # Crear categorías
    categories_data = [
        {"name": "tecnologia", "display_name": "Tecnología"},
        {"name": "educacion", "display_name": "Educación"},
        {"name": "salud", "display_name": "Salud"},
        {"name": "arte", "display_name": "Arte y Cultura"},
        {"name": "deporte", "display_name": "Deportes"},
        {"name": "ciencia", "display_name": "Ciencia"},
    ]
    
    print("📂 Creando categorías...")
    for cat_data in categories_data:
        category, created = Category.objects.get_or_create(
            name=cat_data["name"],
            defaults={"display_name": cat_data["display_name"]}
        )
        if created:
            print(f"   ✅ Categoría creada: {category.display_name}")
        else:
            print(f"   ℹ️  Categoría existente: {category.display_name}")
    
    # Crear organizaciones
    organizations_data = [
        {"name": "Universidad Nacional", "description": "Institución educativa de alta calidad"},
        {"name": "TechHub Colombia", "description": "Comunidad de tecnología e innovación"},
        {"name": "Ministerio de Salud", "description": "Entidad gubernamental de salud pública"},
        {"name": "Centro Cultural Metropolitan", "description": "Espacio para eventos culturales y artísticos"},
        {"name": "Liga Deportiva Regional", "description": "Organización deportiva regional"},
        {"name": "Instituto de Investigación", "description": "Centro de investigación científica"},
    ]
    
    print("🏢 Creando organizaciones...")
    for org_data in organizations_data:
        organization, created = Organization.objects.get_or_create(
            name=org_data["name"],
            defaults={"description": org_data["description"]}
        )
        if created:
            print(f"   ✅ Organización creada: {organization.name}")
        else:
            print(f"   ℹ️  Organización existente: {organization.name}")
    
    # Crear eventos de ejemplo
    events_data = [
        {
            "name": "Conferencia de Inteligencia Artificial 2025",
            "date": datetime.now().date() + timedelta(days=15),
            "time": "09:00",
            "modality": "hibrido",
            "location": "Auditorio Principal - Universidad Nacional",
            "organization": "Universidad Nacional",
            "category": "tecnologia",
            "type": "conferencia",
            "image": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e",
            "description": "Una conferencia sobre los últimos avances en inteligencia artificial y machine learning, dirigida a profesionales y estudiantes del área.",
            "link": "https://ejemplo.com/conferencia-ia"
        },
        {
            "name": "Workshop de Desarrollo Web Full Stack",
            "date": datetime.now().date() + timedelta(days=7),
            "time": "14:00",
            "modality": "presencial",
            "location": "Centro de Innovación TechHub",
            "organization": "TechHub Colombia",
            "category": "tecnologia",
            "type": "workshop",
            "image": "https://images.unsplash.com/photo-1555066931-4365d14bab8c",
            "description": "Aprende a desarrollar aplicaciones web completas usando tecnologías modernas como React, Node.js y MongoDB.",
            "link": "https://ejemplo.com/workshop-fullstack"
        },
        {
            "name": "Simposio de Salud Pública",
            "date": datetime.now().date() + timedelta(days=22),
            "time": "08:30",
            "modality": "virtual",
            "location": "Plataforma Zoom",
            "organization": "Ministerio de Salud",
            "category": "salud",
            "type": "simposio",
            "image": "https://images.unsplash.com/photo-1584515933487-779824d29309",
            "description": "Simposio sobre políticas de salud pública y prevención de enfermedades, dirigido a profesionales de la salud.",
            "link": "https://ejemplo.com/simposio-salud"
        },
        {
            "name": "Festival de Arte Contemporáneo",
            "date": datetime.now().date() + timedelta(days=30),
            "time": "18:00",
            "modality": "presencial",
            "location": "Centro Cultural Metropolitan",
            "organization": "Centro Cultural Metropolitan",
            "category": "arte",
            "type": "festival",
            "image": "https://images.unsplash.com/photo-1513475382585-d06e58bcb0e0",
            "description": "Festival que reúne artistas contemporáneos de toda la región, con exposiciones, performances y talleres.",
            "link": "https://ejemplo.com/festival-arte"
        },
        {
            "name": "Maratón Benéfica 2025",
            "date": datetime.now().date() + timedelta(days=45),
            "time": "06:00",
            "modality": "presencial",
            "location": "Parque Central de la Ciudad",
            "organization": "Liga Deportiva Regional",
            "category": "deporte",
            "type": "competencia",
            "image": "https://images.unsplash.com/photo-1544717297-fa95b6ee9643",
            "description": "Maratón benéfica para recaudar fondos para organizaciones sin fines de lucro. Incluye categorías de 5K, 10K y 21K.",
            "link": "https://ejemplo.com/maraton-benefica"
        },
        {
            "name": "Congreso de Investigación Científica",
            "date": datetime.now().date() + timedelta(days=60),
            "time": "09:00",
            "modality": "hibrido",
            "location": "Instituto de Investigación",
            "organization": "Instituto de Investigación",
            "category": "ciencia",
            "type": "congreso",
            "image": "https://images.unsplash.com/photo-1532094349884-543bc11b234d",
            "description": "Congreso que presenta los últimos hallazgos en investigación científica de diversas disciplinas.",
            "link": "https://ejemplo.com/congreso-ciencia"
        }
    ]
    
    print("📅 Creando eventos...")
    for event_data in events_data:
        try:
            organization = Organization.objects.get(name=event_data["organization"])
            category = Category.objects.get(name=event_data["category"])
            
            event, created = Event.objects.get_or_create(
                name=event_data["name"],
                defaults={
                    "date": event_data["date"],
                    "time": event_data["time"],
                    "modality": event_data["modality"],
                    "location": event_data["location"],
                    "organization": organization,
                    "category": category,
                    "type": event_data["type"],
                    "image": event_data["image"],
                    "description": event_data["description"],
                    "link": event_data["link"]
                }
            )
            
            if created:
                print(f"   ✅ Evento creado: {event.name}")
            else:
                print(f"   ℹ️  Evento existente: {event.name}")
                
        except (Organization.DoesNotExist, Category.DoesNotExist) as e:
            print(f"   ❌ Error creando evento {event_data['name']}: {e}")
    
    print("\n🎉 ¡Datos de prueba creados exitosamente!")
    print("\n📊 Resumen:")
    print(f"   📂 Categorías: {Category.objects.count()}")
    print(f"   🏢 Organizaciones: {Organization.objects.count()}")
    print(f"   📅 Eventos: {Event.objects.count()}")
    print("\n🚀 Ahora puedes probar el panel administrativo en:")
    print("   http://127.0.0.1:8000/api/admin-panel/")

if __name__ == "__main__":
    create_sample_data()
