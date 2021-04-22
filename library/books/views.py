from rest_framework import viewsets, permissions

from library.books.models import Author, Book
from library.books.serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Book.objects.all()
        authors = self.request.query_params.get("authors")
        if authors is not None:
            authors = authors.split(",")
            queryset = queryset.filter(authors__name__in=authors)
        return queryset
