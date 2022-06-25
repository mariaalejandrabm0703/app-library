from multiprocessing import context
from venv import create
from django.shortcuts import render, redirect
from django.views import View
from .forms import BookCreateForm, AuthorCreateForm

class LibraryView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'library.html', context={'title': 'Library'})

class BookCreateView(View):
    def get(self, request, *args, **kwargs):
        context={
            'title': 'Create Book',
        }
        return render(request, 'book_create.html', context=context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = BookCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                description = form.cleaned_data.get('description')
                p, created = Post.objects.get_or_create(title=title, description=description)
                p.save()
                return redirect('library:library')

class AuthorCreateView(View):
    def get(self, request, *args, **kwargs):
        context={
            'title': 'Create Author',
        }
        return render(request, 'author_create.html', context=context)
    
    def post(self, request, *args, **kwargs):
        form = AuthorCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'author_create.html', context={'title': 'Create Author', 'form': form})