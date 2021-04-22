from django.contrib import admin

from library.books.models import Author, Book


admin.site.register(Author)
admin.site.register(Book)
