from django.shortcuts import render
from projects.models import Project

def report_dashboard(request):
    total = Project.objects.count()
    completed = Project.objects.filter(status='completed').count()
    in_progress = Project.objects.filter(status='in_progress').count()
    new = Project.objects.filter(status='new').count()

    context = {
        'total': total,
        'completed': completed,
        'in_progress': in_progress,
        'new': new,
    }
    return render(request, 'reports/dashboard.html', context)