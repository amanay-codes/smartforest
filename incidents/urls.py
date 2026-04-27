from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('about/', views.about_view, name='about'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('report/submit/', views.submit_report, name='submit_report'),
    path('report/<int:pk>/', views.report_detail, name='report_detail'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/report/<int:pk>/', views.admin_report_detail, name='admin_report_detail'),
    path('admin-dashboard/statistics/', views.admin_statistics, name='admin_statistics'),
    path('admin-dashboard/users/', views.admin_users, name='admin_users'),
]
