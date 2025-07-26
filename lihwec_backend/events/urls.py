#from django.urls import path
#from . import views
#from .views import index

#urlpatterns = [
#    path('', index),
#    path('events/', views.EventListCreateView.as_view(), name='event-list'),
#    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
#    path('events/search/', views.EventSearchView.as_view(), name='event-search'),
#    path('events/filter/', views.EventFilterView.as_view(), name='event-filter'),
#    path('organizations/', views.OrganizationListView.as_view(), name='organization-list'),
#    path('categories/', views.CategoryListView.as_view(), name='category-list'),
#]

# events/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, CategoryViewSet, OrganizationViewSet, TypeViewSet, EventSearchView, EventFilterView
from .admin_views import (
    AdminPanelView, EventManagementView, OrganizationManagementView, CategoryManagementView,
    AdminEventAPIView, AdminOrganizationAPIView, AdminCategoryAPIView
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'types', TypeViewSet)
# No registramos events en el router para evitar conflictos con las rutas personalizadas

urlpatterns = [
    # Panel Administrativo
    path('admin-panel/', AdminPanelView.as_view(), name='admin_panel'),
    path('admin-panel/events/', EventManagementView.as_view(), name='event_management'),
    path('admin-panel/organizations/', OrganizationManagementView.as_view(), name='organization_management'),
    path('admin-panel/categories/', CategoryManagementView.as_view(), name='category_management'),
    
    # APIs del Panel Administrativo
    path('admin/api/events/', AdminEventAPIView.as_view(), name='admin_event_api'),
    path('admin/api/events/<int:event_id>/', AdminEventAPIView.as_view(), name='admin_event_detail_api'),
    path('admin/api/organizations/', AdminOrganizationAPIView.as_view(), name='admin_org_api'),
    path('admin/api/organizations/<int:org_id>/', AdminOrganizationAPIView.as_view(), name='admin_org_detail_api'),
    path('admin/api/categories/', AdminCategoryAPIView.as_view(), name='admin_cat_api'),
    path('admin/api/categories/<int:cat_id>/', AdminCategoryAPIView.as_view(), name='admin_cat_detail_api'),
    
    # Endpoints personalizados ANTES del router
    path('events/search/', EventSearchView.as_view(), name='event-search'),
    path('events/filter/', EventFilterView.as_view(), name='event-filter'),
    
    # Endpoints del ViewSet para eventos
    path('events/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='event-list'),
    path('events/<int:pk>/', EventViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='event-detail'),
    
    # Incluir el router para categories y organizations
    path('', include(router.urls)),
]
