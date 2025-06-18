from django.shortcuts import render
from .models import Staff


def staff_list(request):
    staff_members = Staff.objects.select_related('user_profile__user').all()
    return render(request, 'staff/list.html', {'staff': staff_members})