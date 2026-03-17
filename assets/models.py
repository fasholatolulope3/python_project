from django.db import models

class Asset(models.Model):
    """Tracks company IT hardware (Laptops, Servers, Printers)."""
    ASSET_TYPES = [
        ('LAPTOP', 'Laptop'),
        ('SERVER', 'Server'),
        ('NETWORK', 'Network Device'),
        ('OTHER', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPES, default='LAPTOP')
    serial_number = models.CharField(max_length=100, unique=True)
    assigned_to = models.CharField(max_length=100, blank=True)
    purchase_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

class Ticket(models.Model):
    """Tracks technical issues and troubleshooting progress."""
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('URGENT', 'Urgent'),
    ]
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='tickets')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='MEDIUM')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Service(models.Model):
    """Tracks third-party integrations and digital platforms."""
    name = models.CharField(max_length=100) # e.g., Paystack, AWS, Web Hosting
    provider = models.CharField(max_length=100)
    status = models.BooleanField(default=True) # True = Active/Up, False = Down/Issue
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name
