from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('profile/', views.profile_view, name='profile'),
    path('manuscripts/list/', views.manuscript_list, name='manuscript-list'),
    path('manuscripts/upload/', views.manuscript_upload, name='manuscript-upload'),
]