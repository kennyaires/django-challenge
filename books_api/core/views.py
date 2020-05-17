from rest_framework.permissions import AllowAny
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorViewSet(ListModelMixin, GenericViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        """Filter by authors name"""
        queryset = Author.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = [AllowAny]
