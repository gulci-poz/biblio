from rest_framework import viewsets, permissions

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

"""
API endpoints
"""


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
