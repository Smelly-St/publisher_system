from django.shortcuts import render, redirect
from projects.models import Project
from authors.models import Author
from tasks.models import Task
from manuscripts.models import Manuscript


def home_view(request):
    total_projects = Project.objects.count()
    active_projects = Project.objects.filter(status='in_progress').count()
    completed_projects = Project.objects.filter(status='completed').count()
    total_authors = Author.objects.count()

    recent_projects = Project.objects.order_by('-start_date')[:3]
    recent_tasks = Task.objects.order_by('-id')[:3]

    context = {
        'total_projects': total_projects,
        'active_projects': active_projects,
        'completed_projects': completed_projects,
        'total_authors': total_authors,
        'recent_projects': recent_projects,
        'recent_tasks': recent_tasks,
    }

    return render(request, 'pages/home_admin.html', context)


def profile_view(request):
    user = request.user
    return render(request, 'pages/profile.html', {'user': user})


def manuscript_list(request):
    manuscripts = Manuscript.objects.all().select_related('project')
    return render(request, 'manuscripts/list.html', {'manuscripts': manuscripts})


def manuscript_upload(request):
    from manuscripts.forms import ManuscriptForm
    form = ManuscriptForm()
    return render(request, 'manuscripts/upload_form.html', {'form': form})