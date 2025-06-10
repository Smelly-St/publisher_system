from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, project_list, project_create
from . import views

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),                  # API: /api/projects/
    path('list/', project_list, name='project-list'), # HTML: /projects/list/
    path('create/', project_create, name='project-create'),  # Новый маршрут: /projects/create/
    path('project/edit/<int:pk>/', views.project_edit, name='project-edit'),
]