#!/usr/bin/env python
"""
Script para actualizar los eventos existentes con los nuevos tipos
"""

import os
import sys
import django

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lihwec_backend.settings')
django.setup()

from events.models import Event

def update_event_types():
    print("🔄 Actualizando tipos de eventos existentes...")
    
    # Mapear tipos antiguos a nuevos tipos
    type_mapping = {
        'workshop': 'difusor',
        'conferencia': 'difusor',
        'seminario': 'difusor',
        'mesa_redonda': 'difusor',
        'hackathon': 'competencia',
        'competencia': 'competencia',
        'torneo': 'competencia',
        'concurso': 'competencia',
    }
    
    eventos_actualizados = 0
    eventos_sin_cambio = 0
    
    for evento in Event.objects.all():
        tipo_actual = evento.type.lower()
        nuevo_tipo = None
        
        # Buscar mapeo exacto
        if tipo_actual in type_mapping:
            nuevo_tipo = type_mapping[tipo_actual]
        else:
            # Buscar por palabras clave
            if any(keyword in tipo_actual for keyword in ['hack', 'competencia', 'concurso', 'torneo']):
                nuevo_tipo = 'competencia'
            else:
                # Por defecto, asignar como difusor
                nuevo_tipo = 'difusor'
        
        if evento.type != nuevo_tipo:
            print(f"   📝 '{evento.name}': '{evento.type}' → '{nuevo_tipo}'")
            evento.type = nuevo_tipo
            evento.save()
            eventos_actualizados += 1
        else:
            eventos_sin_cambio += 1
    
    print(f"\n✅ Actualización completada:")
    print(f"   📝 Eventos actualizados: {eventos_actualizados}")
    print(f"   ✅ Eventos sin cambio: {eventos_sin_cambio}")
    
    # Mostrar resumen por tipo
    print(f"\n📊 Resumen por tipo:")
    competencias = Event.objects.filter(type='competencia').count()
    difusores = Event.objects.filter(type='difusor').count()
    print(f"   🏆 Competencias: {competencias}")
    print(f"   📢 Difusores: {difusores}")

if __name__ == "__main__":
    update_event_types()
