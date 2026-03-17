from django.urls import path
from . import views

urlpatterns = [
    # Asset endpoints
    path('assets/', views.AssetListCreateView.as_view(), name='asset-list'),
    path('assets/<int:pk>/', views.AssetDetailView.as_view(), name='asset-detail'),

    # Ticket endpoints
    path('tickets/', views.TicketListCreateView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', views.TicketDetailView.as_view(), name='ticket-detail'),

    # Service endpoints
    path('services/', views.ServiceListCreateView.as_view(), name='service-list'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service-detail'),
]
