from django.contrib import admin
from django.urls import path

from library.views import AuthorCreateView, AuthorListView, BookCreateView, LibraryView, BookListView

app_name = "library"

urlpatterns = [
    path('', LibraryView.as_view(), name='library'),
    path('book/', BookListView.as_view(), name='book'),
    path('author/', AuthorListView.as_view(), name='author'),
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
]
