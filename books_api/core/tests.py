from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


AUTHORS_URL = reverse('core:author-list')
BOOKS_URL = reverse('core:book-list')


class PublicApiTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        
        # Creates test authors
        Author.objects.bulk_create(
            [Author(name="Anthony Robbins"),
            Author(name="Napoleon Hill"),
            Author(name="Robert Kiyosaki")])

    def test_retrieve_authors_list(self):
        """Test retrieving the list of authors"""

        res = self.client.get(AUTHORS_URL)

        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_and_get_book_successful(self):
        """Test creating a new book and getting info of it"""
        payload = dict(name='Rich Dad Poor Dad', edition='5', publication_year=1999, authors=[3])
        self.client.post(BOOKS_LIST_URL, payload)

        exists = Book.objects.filter(name=payload['name']).exists()
        self.assertTrue(exists)

        res = self.client.get(BOOKS_LIST_URL)
        serializer = BookSerializer(Book.objects.filter(name=payload['name']).first())
        self.assertIn(serializer.data, res.data)
