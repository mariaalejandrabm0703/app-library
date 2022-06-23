from django.shortcuts import render
from django.views import View

class LibraryView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'library.html', context={'title': 'Library'})
