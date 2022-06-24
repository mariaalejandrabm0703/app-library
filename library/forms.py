from django import forms

from .models import Book, Author

class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'description', 'authors']

class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']