from django.urls import path
from .views import report_dashboard

urlpatterns = [
    path('dashboard/', report_dashboard, name='report-dashboard'),
]