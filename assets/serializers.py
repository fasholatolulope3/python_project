from rest_framework import serializers
from .models import Asset, Ticket, Service

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'

class TicketSerializer(serializers.ModelSerializer):
    # We display the asset name in the ticket for better readability
    asset_name = serializers.ReadOnlyField(source='asset.name')
    
    class Meta:
        model = Ticket
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
