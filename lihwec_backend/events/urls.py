from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event-detail'),
    path('events/search/', views.EventSearchView.as_view(), name='event-search'),
    path('events/filter/', views.EventFilterView.as_view(), name='event-filter'),
    path('organizations/', views.OrganizationListView.as_view(), name='organization-list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
]