from django.contrib import admin
from django.urls import path, include
from pages.views import home_view
from django.contrib.auth import views as auth_views


urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    # Маршруты модулей
    path('', home_view, name='home'),
    path('', include('pages.urls')),
    path('projects/', include('projects.urls', namespace='projects')),
    path('authors/', include('authors.urls')),
    path('tasks/', include('tasks.urls')),
    path('manuscripts/', include('manuscripts.urls')),
    path('accounts/', include('accounts.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]