#!/usr/bin/env bash
# build.sh - Script de construcción para Render

set -o errexit  # exit on error

echo "🚀 Iniciando build process..."

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

# Cambiar al directorio del proyecto Django
echo "📁 Cambiando al directorio del proyecto..."
cd lihwec_backend

# Crear directorio para archivos estáticos si no existe
echo "📂 Creando directorio para archivos estáticos..."
mkdir -p staticfiles

# Recopilar archivos estáticos
echo "🎨 Recopilando archivos estáticos..."
python manage.py collectstatic --no-input

# Ejecutar migraciones
echo "🗃️ Ejecutando migraciones de base de datos..."
python manage.py migrate

# Crear datos de prueba si no existen
echo "🌱 Verificando datos de prueba..."
python manage.py shell -c "
from events.models import Event
if not Event.objects.exists():
    print('📝 Creando datos de prueba...')
    exec(open('create_test_data.py').read())
    print('✅ Datos de prueba creados exitosamente')
else:
    print('ℹ️ Los datos de prueba ya existen')
"

echo "🎉 Build process completado exitosamente!"
