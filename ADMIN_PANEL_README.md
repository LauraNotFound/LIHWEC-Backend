# 🚀 Panel Administrativo LIHWEC

¡Tu panel administrativo está listo! Ahora puedes gestionar todos los eventos, organizaciones y categorías desde una interfaz web moderna y fácil de usar.

## 📋 Instrucciones de Uso

### 1. Iniciar el Servidor

Abre una terminal en el directorio del backend y ejecuta:

```cmd
cd "c:\Users\lcmm9\Desktop\Proyectos\Web\LIHWEC\LIHWEC-Backend\lihwec_backend"
python manage.py runserver
```

### 2. Acceder al Panel Administrativo

Una vez que el servidor esté corriendo, abre tu navegador y ve a:

**🏠 Dashboard Principal:** `http://127.0.0.1:8000/api/admin-panel/`

### 3. Navegación del Panel

El panel incluye las siguientes secciones:

- **📊 Dashboard**: Vista general con estadísticas y eventos recientes
- **📅 Eventos**: Gestión completa de eventos (crear, editar, eliminar)
- **🏢 Organizaciones**: Gestión de organizaciones
- **🏷️ Categorías**: Gestión de categorías

## 🔧 Funcionalidades Disponibles

### ✨ Dashboard

- Estadísticas en tiempo real
- Eventos recientes
- Acceso rápido a todas las secciones
- Resumen de organizaciones y categorías

### 📅 Gestión de Eventos

- ➕ Crear nuevos eventos
- ✏️ Editar eventos existentes
- 🗑️ Eliminar eventos
- 📋 Listar todos los eventos
- 🔍 Ver detalles completos

### 🏢 Gestión de Organizaciones

- ➕ Crear nuevas organizaciones
- ✏️ Editar organizaciones existentes
- 🗑️ Eliminar organizaciones
- 📊 Ver cantidad de eventos por organización

### 🏷️ Gestión de Categorías

- ➕ Crear nuevas categorías
- ✏️ Editar categorías existentes
- 🗑️ Eliminar categorías
- 📊 Ver cantidad de eventos por categoría

## 🌐 URLs del Panel

| Sección        | URL                                                    |
| -------------- | ------------------------------------------------------ |
| Dashboard      | `http://127.0.0.1:8000/api/admin-panel/`               |
| Eventos        | `http://127.0.0.1:8000/api/admin-panel/events/`        |
| Organizaciones | `http://127.0.0.1:8000/api/admin-panel/organizations/` |
| Categorías     | `http://127.0.0.1:8000/api/admin-panel/categories/`    |

## 🔑 APIs del Panel

El panel también incluye APIs específicas para la administración:

### Eventos

- `POST /api/admin/api/events/` - Crear evento
- `PUT /api/admin/api/events/{id}/` - Actualizar evento
- `DELETE /api/admin/api/events/{id}/` - Eliminar evento

### Organizaciones

- `POST /api/admin/api/organizations/` - Crear organización
- `PUT /api/admin/api/organizations/{id}/` - Actualizar organización
- `DELETE /api/admin/api/organizations/{id}/` - Eliminar organización

### Categorías

- `POST /api/admin/api/categories/` - Crear categoría
- `PUT /api/admin/api/categories/{id}/` - Actualizar categoría
- `DELETE /api/admin/api/categories/{id}/` - Eliminar categoría

## 🎨 Características de la Interfaz

- **📱 Responsive**: Funciona en desktop, tablet y móvil
- **🎨 Diseño Moderno**: Interfaz limpia con Bootstrap 5
- **⚡ Tiempo Real**: Actualizaciones inmediatas
- **🔔 Notificaciones**: Alertas de éxito y error
- **🎯 Fácil de Usar**: Navegación intuitiva

## 🛠️ Solución de Problemas

### Problema: Error 404 al acceder al panel

**Solución**: Asegúrate de que el servidor esté corriendo y que accedas a la URL correcta.

### Problema: Error de CORS

**Solución**: El backend ya está configurado para CORS, pero si usas un dominio diferente, añádelo a `ALLOWED_HOSTS` en `settings.py`.

### Problema: Error al guardar datos

**Solución**: Verifica que todos los campos requeridos estén completados y que las organizaciones/categorías existan.

## 🚀 ¡Listo para usar!

Tu panel administrativo está completamente funcional. Puedes:

1. **Crear datos de prueba** usando el panel
2. **Gestionar eventos** fácilmente
3. **Organizar categorías** y organizaciones
4. **Ver estadísticas** en tiempo real

¡Disfruta de tu nuevo panel administrativo LIHWEC! 🎉
