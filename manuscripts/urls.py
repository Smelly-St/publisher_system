from django.urls import path
from . import views

app_name = 'manuscripts'

urlpatterns = [
    path('list/', views.manuscript_list, name='manuscript-list'),
    path('upload/', views.manuscript_upload, name='manuscript-upload'),
    path('<int:pk>/', views.manuscript_detail, name='manuscript-detail'),
]