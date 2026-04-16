from django.db import models
from django.contrib.auth.models import User

INCIDENT_TYPES = [
    ('wildfire', 'Wildfire'),
    ('illegal_logging', 'Illegal Logging'),
    ('pollution', 'Pollution'),
    ('forest_damage', 'Forest Damage'),
]

STATUS_CHOICES = [
    ('pending', 'Pending'),
    ('in_progress', 'In Progress'),
    ('resolved', 'Resolved'),
]

class IncidentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=50, choices=INCIDENT_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='incidents/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    admin_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.incident_type} - {self.location} ({self.status})"