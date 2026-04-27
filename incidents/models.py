from django.db import models
from django.contrib.auth.models import User


class IncidentType(models.TextChoices):
    WILDFIRE = 'wildfire', 'Wildfire'
    ILLEGAL_LOGGING = 'illegal_logging', 'Illegal Logging'
    POLLUTION = 'pollution', 'Pollution'
    FOREST_DAMAGE = 'forest_damage', 'Forest Damage'


class ReportStatus(models.TextChoices):
    PENDING = 'pending', 'Pending'
    IN_PROGRESS = 'in_progress', 'In Progress'
    RESOLVED = 'resolved', 'Resolved'


INCIDENT_TYPES = IncidentType.choices
STATUS_CHOICES = ReportStatus.choices


class IncidentReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    incident_type = models.CharField(max_length=50, choices=IncidentType.choices)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='incidents/', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=ReportStatus.choices,
        default=ReportStatus.PENDING,
    )
    submitted_at = models.DateTimeField(auto_now_add=True)
    admin_notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-submitted_at']
        verbose_name = 'incident report'
        verbose_name_plural = 'incident reports'

    def __str__(self):
        return f"{self.incident_type} - {self.location} ({self.status})"

    @property
    def is_critical(self):
        return (
            self.incident_type in {IncidentType.WILDFIRE, IncidentType.FOREST_DAMAGE}
            and self.status in {ReportStatus.PENDING, ReportStatus.IN_PROGRESS}
        )
