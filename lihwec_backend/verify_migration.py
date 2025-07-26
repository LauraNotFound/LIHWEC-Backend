#!/usr/bin/env python
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lihwec_backend.settings')
django.setup()

from events.models import Event, Type

print("=== Verificación después de la migración ===")

print("\nTipos de eventos creados:")
for type_obj in Type.objects.all():
    print(f"ID: {type_obj.id}, Nombre: '{type_obj.name}'")

print("\nEventos con sus tipos:")
for event in Event.objects.all():
    print(f"ID: {event.id}, Nombre: '{event.name}', Tipo: '{event.type.name}' (Type ID: {event.type.id})")

print("\n=== Verificación completada ===")
