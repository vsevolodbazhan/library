from rest_framework import serializers

from library.books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "description"]
