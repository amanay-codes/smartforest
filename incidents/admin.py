from django.contrib import admin
from .models import IncidentReport

@admin.register(IncidentReport)
class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ['user', 'incident_type', 'location', 'status', 'submitted_at']
    list_filter = ['status', 'incident_type']
    search_fields = ['description', 'location']