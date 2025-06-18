from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('list/', views.staff_list, name='staff-list'),
]