from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import IncidentReport, ReportStatus


class IncidentWorkflowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='citizen',
            email='citizen@example.com',
            password='password12345',
        )
        self.admin = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='password12345',
            is_staff=True,
        )

    def test_user_can_submit_report_to_database(self):
        self.client.force_login(self.user)

        response = self.client.post(reverse('submit_report'), {
            'incident_type': 'wildfire',
            'description': 'Smoke near the north trail.',
            'location': 'North trail',
        })

        self.assertRedirects(response, reverse('dashboard'))
        report = IncidentReport.objects.get(user=self.user)
        self.assertEqual(report.description, 'Smoke near the north trail.')
        self.assertEqual(report.status, ReportStatus.PENDING)

    def test_user_can_only_view_own_report(self):
        other_user = User.objects.create_user(username='other', password='password12345')
        report = IncidentReport.objects.create(
            user=other_user,
            incident_type='pollution',
            description='Dumped waste.',
            location='River edge',
        )
        self.client.force_login(self.user)

        response = self.client.get(reverse('report_detail', args=[report.pk]))

        self.assertEqual(response.status_code, 404)

    def test_admin_can_update_report_status(self):
        report = IncidentReport.objects.create(
            user=self.user,
            incident_type='illegal_logging',
            description='Fresh stumps visible.',
            location='East ridge',
        )
        self.client.force_login(self.admin)

        response = self.client.post(reverse('admin_report_detail', args=[report.pk]), {
            'status': ReportStatus.IN_PROGRESS,
            'admin_notes': 'Ranger team dispatched.',
        })

        self.assertRedirects(response, reverse('admin_dashboard'))
        report.refresh_from_db()
        self.assertEqual(report.status, ReportStatus.IN_PROGRESS)
        self.assertEqual(report.admin_notes, 'Ranger team dispatched.')
