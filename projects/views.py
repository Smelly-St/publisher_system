from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from .forms import ProjectForm


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': projects})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:project-list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/project_form.html', {'form': form, 'form_title': 'Редактирование проекта'})

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects:project-list')
    else:
        form = ProjectForm()

    return render(request, 'projects/project_form.html', {'form': form, 'form_title': 'Новый проект'})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/detail.html', {'project': project})


def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects:project-list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/project_form.html', {'form': form, 'form_title': 'Редактирование проекта'})


def home_view(request):
    total_projects = Project.objects.count()
    active_projects = Project.objects.filter(status='in_progress').count()
    completed_projects = Project.objects.filter(status='completed').count()
    total_authors = Author.objects.count()
    
    recent_projects = Project.objects.order_by('-start_date')[:3]
    recent_tasks = Task.objects.order_by('-created_at')[:5]

    context = {
        'total_projects': total_projects,
        'active_projects': active_projects,
        'completed_projects': completed_projects,
        'total_authors': total_authors,
        'recent_projects': recent_projects,
        'recent_tasks': recent_tasks,
    }

    return render(request, 'pages/home_admin.html', context)