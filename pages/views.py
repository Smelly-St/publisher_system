from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from authors.models import Author
from tasks.models import Task
from manuscripts.models import Manuscript

from projects.forms import ProjectForm
from authors.forms import AuthorForm
from tasks.forms import TaskForm
from manuscripts.forms import ManuscriptForm


# ====== Главная страница ======
def home(request):
    total_projects = Project.objects.count()
    active_projects = Project.objects.filter(status='in_progress').count()
    completed_projects = Project.objects.filter(status='completed').count()
    total_authors = Author.objects.count()

    recent_projects = Project.objects.order_by('-start_date')[:5]
    recent_authors = Author.objects.order_by('-id')[:5]

    context = {
        'total_projects': total_projects,
        'active_projects': active_projects,
        'completed_projects': completed_projects,
        'total_authors': total_authors,
        'recent_projects': recent_projects,
        'recent_authors': recent_authors,
    }

    return render(request, 'pages/home.html', context)


# ====== Проекты ======
def project_list(request):
    # Получаем GET-параметры
    status = request.GET.get('status')
    from_date = request.GET.get('from')
    to_date = request.GET.get('to')

    # Начинаем с полного списка
    projects = Project.objects.all()

    # Фильтруем по статусу
    if status:
        projects = projects.filter(status=status)

    # Фильтруем по датам
    if from_date:
        projects = projects.filter(start_date__gte=from_date)
    if to_date:
        projects = projects.filter(end_date__lte=to_date)

    context = {
        'projects': projects,
        'status': status,
        'from_date': from_date,
        'to_date': to_date,
        'STATUS_CHOICES': Project.STATUS_CHOICES,
    }

    return render(request, 'projects/list.html', context)


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


# ====== Авторы ======
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/list.html', {'authors': authors})


def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorForm()

    return render(request, 'authors/author_form.html', {'form': form})


def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorForm(instance=author)

    return render(request, 'authors/author_form.html', {'form': form})


# ====== Задачи ======
def task_list(request):
    tasks = Task.objects.all().select_related('project', 'assignee')
    return render(request, 'tasks/list.html', {'tasks': tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm()

    return render(request, 'tasks/task_form.html', {'form': form, 'form_title': 'Новая задача'})


def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'tasks/task_form.html', {'form': form, 'form_title': 'Редактировать задачу'})


# ====== Рукописи ======
def manuscript_upload(request):
    if request.method == "POST":
        form = ManuscriptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manuscript-list')
    else:
        form = ManuscriptForm()

    return render(request, 'manuscripts/upload_form.html', {'form': form})


def manuscript_list(request):
    manuscripts = Manuscript.objects.all().select_related('project')
    return render(request, 'manuscripts/list.html', {'manuscripts': manuscripts})