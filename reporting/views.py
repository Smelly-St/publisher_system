from django.shortcuts import render
from projects.models import Project


def report_dashboard(request):
    total = Project.objects.count()
    new = Project.objects.filter(status='new').count()
    in_progress = Project.objects.filter(status='in_progress').count()
    completed = Project.objects.filter(status='completed').count()

    context = {
        'total': total,
        'new': new,
        'in_progress': in_progress,
        'completed': completed,
    }

    return render(request, 'reporting/dashboard.html', context)