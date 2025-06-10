from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import profile_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('projects.urls')),
    path('', include('pages.urls')), 
    path('reports/', include('reporting.urls')),
    path('profile/', profile_view, name='profile'),
]

# Добавляем маршруты для медиафайлов только в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)