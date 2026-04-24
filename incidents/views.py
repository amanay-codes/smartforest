from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Count, Q

from .models import IncidentReport, ReportStatus
from .forms import IncidentReportForm, RegistrationForm, StatusUpdateForm

def is_admin(user):
    return user.is_authenticated and user.is_staff

# AUTH VIEWS
def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
        for error in form.errors.values():
            messages.error(request, error[0])
            return redirect('register')
    return render(request, 'incidents/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            return redirect('dashboard')
        messages.error(request, 'Invalid username or password')
    return render(request, 'incidents/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# USER VIEWS
@login_required
def dashboard(request):
    reports = IncidentReport.objects.filter(user=request.user)
    pending_count = reports.filter(status=ReportStatus.PENDING).count()
    return render(request, 'incidents/dashboard.html', {
        'reports': reports,
        'pending_count': pending_count,
    })

@login_required
def submit_report(request):
    if request.method == 'POST':
        form = IncidentReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            messages.success(request, 'Report submitted successfully!')
            return redirect('dashboard')
    else:
        form = IncidentReportForm()
    return render(request, 'incidents/submit_report.html', {'form': form})

@login_required
def report_detail(request, pk):
    report = get_object_or_404(IncidentReport, pk=pk, user=request.user)
    return render(request, 'incidents/report_detail.html', {'report': report})

# ADMIN VIEWS
@user_passes_test(is_admin, login_url='login')
def admin_dashboard(request):
    reports = IncidentReport.objects.select_related('user')
    incident_type = request.GET.get('incident_type')
    status = request.GET.get('status')
    keyword = request.GET.get('keyword')
    if incident_type:
        reports = reports.filter(incident_type=incident_type)
    if status:
        reports = reports.filter(status=status)
    if keyword:
        reports = reports.filter(
            Q(description__icontains=keyword)
            | Q(location__icontains=keyword)
            | Q(user__username__icontains=keyword)
        )
    total = reports.count()
    return render(request, 'incidents/admin_dashboard.html', {
        'reports': reports,
        'total': total,
    })

@user_passes_test(is_admin, login_url='login')
def admin_report_detail(request, pk):
    report = get_object_or_404(IncidentReport.objects.select_related('user'), pk=pk)
    form = StatusUpdateForm(instance=report)
    if request.method == 'POST':
        form = StatusUpdateForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report updated successfully!')
            return redirect('admin_dashboard')
    return render(request, 'incidents/admin_report_detail.html', {
        'report': report,
        'form': form
    })

@user_passes_test(is_admin, login_url='login')
def admin_statistics(request):
    total = IncidentReport.objects.count()
    by_type = IncidentReport.objects.values('incident_type').annotate(count=Count('id')).order_by('incident_type')
    by_status = IncidentReport.objects.values('status').annotate(count=Count('id')).order_by('status')
    return render(request, 'incidents/admin_statistics.html', {
        'total': total,
        'by_type': by_type,
        'by_status': by_status,
    })

@user_passes_test(is_admin, login_url='login')
def admin_users(request):
    users = User.objects.annotate(report_count=Count('incidentreport')).order_by('-date_joined')
    return render(request, 'incidents/admin_users.html', {'users': users})
