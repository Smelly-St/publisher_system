from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from projects.models import Project
from authors.models import Author
from tasks.models import Task
from manuscripts.models import Manuscript
from .models import UserProfile
from django.contrib.admin.models import LogEntry
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User


@login_required
def profile_view(request):
    user = request.user

    # Создаем профиль пользователя, если его нет
    profile, created = UserProfile.objects.get_or_create(user=user)

    # Статистика проектов
    total_projects = Project.objects.filter(manager__user=user).count()
    active_projects = Project.objects.filter(manager__user=user, status='in_progress').count()
    completed_projects = Project.objects.filter(manager__user=user, status='completed').count()

    # История действий
    project_content_type = ContentType.objects.get_for_model(Project)
    author_content_type = ContentType.objects.get_for_model(Author)
    task_content_type = ContentType.objects.get_for_model(Task)
    manuscript_content_type = ContentType.objects.get_for_model(Manuscript)

    logs = LogEntry.objects.filter(
        user=user,
        content_type__in=[
            project_content_type.id,
            author_content_type.id,
            task_content_type.id,
            manuscript_content_type.id
        ]
    ).select_related('content_type').order_by('-action_time')[:10]

    context = {
        'user': user,
        'profile': profile,
        'total_projects': total_projects,
        'active_projects': active_projects,
        'completed_projects': completed_projects,
        'logs': logs,
    }

    return render(request, 'accounts/profile.html', context)