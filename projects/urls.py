from django.urls import path
from projects import views

app_name = 'projects'

urlpatterns = [
    path('list/', views.project_list, name='project-list'),
    path('create/', views.project_create, name='project-create'),
    path('<int:pk>/edit/', views.project_edit, name='project-edit'),
     path('<int:pk>/', views.project_detail, name='project-detail'),
]