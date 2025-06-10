from pages.views import author_list, author_create

urlpatterns += [
    path('authors/list/', author_list, name='author-list'),
    path('authors/create/', author_create, name='author-create'),
]