from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Manuscript
from .forms import ManuscriptForm


@login_required
def manuscript_list(request):
    manuscripts = Manuscript.objects.all().select_related('project')
    return render(request, 'manuscripts/list.html', {'manuscripts': manuscripts})


@login_required
def manuscript_upload(request):
    if request.method == "POST":
        form = ManuscriptForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manuscripts:manuscript-list')
    else:
        form = ManuscriptForm()

    return render(request, 'manuscripts/upload_form.html', {'form': form, 'form_title': 'Загрузить рукопись'})


@login_required
def manuscript_detail(request, pk):
    manuscript = get_object_or_404(Manuscript, pk=pk)
    return render(request, 'manuscripts/detail.html', {'manuscript': manuscript})