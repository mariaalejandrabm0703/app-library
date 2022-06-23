from django.contrib import admin
from django.urls import path

from library.views import LibraryView

app_name = "library"

urlpatterns = [
    path('', LibraryView.as_view(), name='library'),
]
