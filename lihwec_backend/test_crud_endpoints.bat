@echo off
REM Script para probar endpoints CRUD de la API LIHWEC
REM Asegurate de tener el servidor corriendo: python manage.py runserver

echo === Pruebas de endpoints CRUD ===
echo.

echo 1. Listando todos los tipos existentes...
curl -X GET http://localhost:8000/types/
echo.
echo.

echo 2. Creando un nuevo tipo...
curl -X POST http://localhost:8000/types/ ^
  -H "Content-Type: application/json" ^
  -d "{\"name\": \"seminario\"}"
echo.
echo.

echo 3. Listando tipos después de crear uno nuevo...
curl -X GET http://localhost:8000/types/
echo.
echo.

echo 4. Actualizando el tipo con ID 7 (asumiendo que es el que creamos)...
curl -X PUT http://localhost:8000/types/7/ ^
  -H "Content-Type: application/json" ^
  -d "{\"name\": \"seminario_actualizado\"}"
echo.
echo.

echo 5. Obteniendo el tipo específico...
curl -X GET http://localhost:8000/types/7/
echo.
echo.

echo 6. Listando todos los eventos...
curl -X GET http://localhost:8000/events/
echo.
echo.

echo 7. Actualizando campos específicos del evento con ID 1 (PATCH)...
curl -X PATCH http://localhost:8000/events/1/ ^
  -H "Content-Type: application/json" ^
  -d "{\"name\": \"Evento Actualizado con PATCH\", \"location\": \"Nueva ubicacion\"}"
echo.
echo.

echo 8. Eliminando el tipo que creamos (ID 7)...
curl -X DELETE http://localhost:8000/types/7/
echo.
echo.

echo 9. Verificando que el tipo fue eliminado (debería dar error 404)...
curl -X GET http://localhost:8000/types/7/
echo.
echo.

echo === Pruebas completadas ===
pause
