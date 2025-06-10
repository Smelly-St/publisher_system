from authors.models import Author
from authors.forms import AuthorForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'authors/list.html', {'authors': authors})

def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author-list')
    else:
        form = AuthorForm()

    return render(request, 'authors/author_form.html', {'form': form})