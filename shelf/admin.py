from django.contrib import admin

from .models import Author, BookCategory, Book, BookEdition, BookItem, Publisher


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ['last_name', 'first_name']
    # sortowanie w malejącym porządku: '-last_name'
    ordering = ['last_name']


class BookAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title']

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register([BookCategory, BookItem, BookEdition, Publisher])
