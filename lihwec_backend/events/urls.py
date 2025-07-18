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
from .views import EventViewSet, CategoryViewSet, OrganizationViewSet, EventSearchView, EventFilterView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'organizations', OrganizationViewSet)
# No registramos events en el router para evitar conflictos con las rutas personalizadas

urlpatterns = [
    # Endpoints personalizados ANTES del router
    path('events/search/', EventSearchView.as_view(), name='event-search'),
    path('events/filter/', EventFilterView.as_view(), name='event-filter'),
    
    # Endpoints del ViewSet para eventos
    path('events/', EventViewSet.as_view({'get': 'list', 'post': 'create'}), name='event-list'),
    path('events/<int:pk>/', EventViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='event-detail'),
    
    # Incluir el router para categories y organizations
    path('', include(router.urls)),
]
