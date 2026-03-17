from rest_framework import generics
from .models import Asset, Ticket, Service
from .serializers import AssetSerializer, TicketSerializer, ServiceSerializer

# --- ASSET VIEWS ---
class AssetListCreateView(generics.ListCreateAPIView):
    """List all assets or create a new one."""
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete an asset."""
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer


# --- TICKET VIEWS ---
class TicketListCreateView(generics.ListCreateAPIView):
    """List all tickets or create a new one."""
    queryset = Ticket.objects.all().order_by('-priority', '-created_at')
    serializer_class = TicketSerializer

class TicketDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a ticket."""
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


# --- SERVICE VIEWS ---
class ServiceListCreateView(generics.ListCreateAPIView):
    """List all services or create a new one."""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a service."""
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
