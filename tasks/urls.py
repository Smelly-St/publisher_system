from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('list/', views.task_list, name='task-list'),
    path('create/', views.task_create, name='task-create'),
    path('<int:pk>/edit/', views.task_edit, name='task-edit'),
]