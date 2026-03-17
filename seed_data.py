import os
import django
import sys

# Setup Django environment
sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
django.setup()

from assets.models import Asset, Ticket, Service

def seed():
    print("🌱 Seeding database with professional sample data...")
    
    # Clear existing data
    Asset.objects.all().delete()
    Ticket.objects.all().delete()
    Service.objects.all().delete()

    # 1. Create Assets
    laptop1 = Asset.objects.create(
        name="MacBook Pro - Tolulope",
        asset_type="LAPTOP",
        serial_number="VEMRE-LP-001",
        assigned_to="Tolulope Fashola"
    )
    
    server1 = Asset.objects.create(
        name="Main Production Server",
        asset_type="SERVER",
        serial_number="VEMRE-SRV-99",
        assigned_to="IT Department"
    )
    
    Asset.objects.create(
        name="Office Router",
        asset_type="NETWORK",
        serial_number="VEMRE-NET-05",
        assigned_to="Admin"
    )

    # 2. Create Tickets
    Ticket.objects.create(
        title="Software License Renewal",
        description="Renew the Microsoft 365 license for the design team.",
        asset=laptop1,
        priority="MEDIUM",
        status="IN_PROGRESS"
    )
    
    Ticket.objects.create(
        title="Server Overheating Warning",
        description="Sensor in Rack 4 reporting high temperature.",
        asset=server1,
        priority="URGENT",
        status="OPEN"
    )
    
    Ticket.objects.create(
        title="VPN Connection Issues",
        description="Remote workers reporting 404 errors on the internal portal.",
        asset=server1,
        priority="HIGH",
        status="OPEN"
    )

    # 3. Create Services
    Service.objects.create(name="Paystack API", provider="Paystack", status=True)
    Service.objects.create(name="AWS EC2 Instances", provider="Amazon Web Services", status=True)
    Service.objects.create(name="Office Internet", provider="MTN Business", status=True, notes="Main line is stable")

    print("✅ Seeding complete! Your dashboard is now alive.")

if __name__ == '__main__':
    seed()
