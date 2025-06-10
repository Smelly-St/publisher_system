from django.urls import path
from pages.views import (
    home,
    project_list,
    project_create,
    project_edit,
    author_list,
    author_create,
    author_edit,
    task_list,
    task_create,
    task_edit,
    manuscript_list,
    manuscript_upload,
)

urlpatterns = [
    # Главная страница
    path('', home, name='home'),

    # Проекты
    path('projects/list/', project_list, name='project-list'),
    path('projects/create/', project_create, name='project-create'),
    path('projects/edit/<int:pk>/', project_edit, name='project-edit'),

    # Авторы
    path('authors/list/', author_list, name='author-list'),
    path('authors/create/', author_create, name='author-create'),
    path('authors/edit/<int:pk>/', author_edit, name='author-edit'),

    # Задачи
    path('tasks/list/', task_list, name='task-list'),
    path('tasks/create/', task_create, name='task-create'),
    path('tasks/edit/<int:pk>/', task_edit, name='task-edit'),

    # Рукописи
    path('manuscripts/list/', manuscript_list, name='manuscript-list'),  # ✅ Эта строчка должна быть
    path('manuscripts/upload/', manuscript_upload, name='manuscript-upload'),
]