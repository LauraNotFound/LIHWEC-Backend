#!/usr/bin/env python
"""
Script de ejemplo para probar los endpoints CRUD de la API LIHWEC
Asegúrate de tener el servidor corriendo: python manage.py runserver
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_crud_operations():
    print("=== Pruebas de endpoints CRUD ===\n")
    
    # 1. Crear un nuevo tipo
    print("1. Creando un nuevo tipo...")
    new_type_data = {"name": "seminario"}
    response = requests.post(f"{BASE_URL}/types/", json=new_type_data)
    if response.status_code == 201:
        type_id = response.json()['id']
        print(f"✅ Tipo creado con ID: {type_id}")
        print(f"   Respuesta: {response.json()}")
    else:
        print(f"❌ Error creando tipo: {response.status_code}")
        return
    
    # 2. Listar todos los tipos
    print("\n2. Listando todos los tipos...")
    response = requests.get(f"{BASE_URL}/types/")
    if response.status_code == 200:
        types = response.json()
        print(f"✅ Se encontraron {len(types)} tipos:")
        for t in types:
            print(f"   - ID: {t['id']}, Nombre: {t['name']}")
    
    # 3. Actualizar el tipo creado
    print(f"\n3. Actualizando el tipo con ID {type_id}...")
    update_data = {"name": "seminario_actualizado"}
    response = requests.put(f"{BASE_URL}/types/{type_id}/", json=update_data)
    if response.status_code == 200:
        print(f"✅ Tipo actualizado: {response.json()}")
    else:
        print(f"❌ Error actualizando tipo: {response.status_code}")
    
    # 4. Obtener el tipo específico
    print(f"\n4. Obteniendo el tipo con ID {type_id}...")
    response = requests.get(f"{BASE_URL}/types/{type_id}/")
    if response.status_code == 200:
        print(f"✅ Tipo obtenido: {response.json()}")
    
    # 5. Eliminar el tipo
    print(f"\n5. Eliminando el tipo con ID {type_id}...")
    response = requests.delete(f"{BASE_URL}/types/{type_id}/")
    if response.status_code == 204:
        print("✅ Tipo eliminado exitosamente")
    else:
        print(f"❌ Error eliminando tipo: {response.status_code}")
    
    # 6. Verificar que fue eliminado
    print(f"\n6. Verificando que el tipo fue eliminado...")
    response = requests.get(f"{BASE_URL}/types/{type_id}/")
    if response.status_code == 404:
        print("✅ Confirmado: el tipo ya no existe")
    else:
        print(f"❌ El tipo todavía existe: {response.status_code}")

def test_event_operations():
    print("\n=== Pruebas con eventos ===\n")
    
    # Obtener el primer evento para modificarlo
    response = requests.get(f"{BASE_URL}/events/")
    if response.status_code == 200:
        events = response.json()
        if events:
            event_id = events[0]['id']
            print(f"Usando evento con ID: {event_id}")
            
            # Actualizar solo algunos campos con PATCH
            print(f"\n1. Actualizando campos específicos del evento {event_id}...")
            patch_data = {
                "name": "Evento Actualizado con PATCH",
                "location": "Nueva ubicación"
            }
            response = requests.patch(f"{BASE_URL}/events/{event_id}/", json=patch_data)
            if response.status_code == 200:
                print(f"✅ Evento actualizado: {response.json()['name']}")
            else:
                print(f"❌ Error actualizando evento: {response.status_code}")

if __name__ == "__main__":
    try:
        test_crud_operations()
        test_event_operations()
        print("\n=== Todas las pruebas completadas ===")
    except requests.exceptions.ConnectionError:
        print("❌ Error: No se pudo conectar al servidor.")
        print("   Asegúrate de que el servidor esté corriendo: python manage.py runserver")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
