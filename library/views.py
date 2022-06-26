from django.shortcuts import render, redirect
from django.views import View

from library.models import Author, Book
from .forms import BookCreateForm, AuthorCreateForm

class LibraryView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'library.html', context={'title': 'Library'})

class BookListView(View):
    def get(self, request, *args, **kwargs):
        books=Book.objects.all()
        context={
            'title': 'List Book',
            'books': books
        }
        return render(request, 'book_list.html', context=context)

class BookCreateView(View):
    def get(self, request, *args, **kwargs):
        form = BookCreateForm()
        context={
            'form': form,
        }
        return render(request, 'book_create.html', context=context)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = BookCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                description = form.cleaned_data.get('description')
                p, created = Book.objects.get_or_create(title=title, description=description)
                p.save()
                return redirect('library:book')
class AuthorListView(View):
    def get(self, request, *args, **kwargs):
        authors=Author.objects.all()
        context={
            'title': 'List Author',
            'authors': authors
        }
        return render(request, 'author_list.html', context=context)
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