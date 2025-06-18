from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('list/', views.author_list, name='author-list'),
    path('create/', views.author_create, name='author-create'),
    path('<int:pk>/edit/', views.author_edit, name='author-edit'),
]