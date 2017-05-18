from django.contrib import admin

from .models import Author, Book, Publisher

admin.site.register([Author, Book, Publisher])
