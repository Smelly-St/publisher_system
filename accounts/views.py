from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserProfile


@login_required
def profile_view(request):
    user_profile = request.user.userprofile
    return render(request, 'accounts/profile.html', {'user_profile': user_profile})