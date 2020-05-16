from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
