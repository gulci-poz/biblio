from django.contrib import admin

from .models import Author, Book, Publisher


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    # sortowanie w malejącym porządku: '-last_name'
    ordering = ['last_name']


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']
    # zmieniony model usuwam 'author', 'isbn' oraz 'publisher'

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register([Publisher])
