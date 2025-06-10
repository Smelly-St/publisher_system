# ====== API ViewSet для REST API ======
from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


# ====== Форма и HTML-представления ======
from django.shortcuts import render, redirect, get_object_or_404
from .models import Project
from django import forms
from django.forms import ModelForm

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': projects})

def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        form = ProjectForm()

    return render(request, 'projects/project_form.html', {'form': form})

def project_edit(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project-list')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'projects/project_form.html', {'form': form})