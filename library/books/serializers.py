from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer

from library.books.models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class BookSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = ["id", "title", "description", "authors"]
