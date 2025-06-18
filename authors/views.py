from django.shortcuts import render, redirect, get_object_or_404
from .models import Author
from .forms import AuthorForm


def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/list.html', {'authors': authors})


def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorForm()

    return render(request, 'authors/author_form.html', {'form': form, 'form_title': 'Новый автор'})


def author_edit(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == "POST":
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorForm(instance=author)

    return render(request, 'authors/author_form.html', {
        'form': form,
        'form_title': 'Редактировать автора',
        'author': author
    })