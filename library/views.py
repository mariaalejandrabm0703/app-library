from django.shortcuts import render
from django.views import View
from .forms import BookCreateForm, AuthorCreateForm

class LibraryView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'library.html', context={'title': 'Library'})

class BookCreateView(View):
    def get(self, request, *args, **kwargs):
        form = BookCreateForm()
        return render(request, 'book_create.html', context={'title': 'Create Book', 'form': form})

    def post(self, request, *args, **kwargs):
        form = BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'book_create.html', context={'title': 'Create Book', 'form': form})

class AuthorCreateView(View):
    def get(self, request, *args, **kwargs):
        form = AuthorCreateForm()
        return render(request, 'author_create.html', context={'title': 'Create Author', 'form': form})
    
    def post(self, request, *args, **kwargs):
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'author_create.html', context={'title': 'Create Author', 'form': form})