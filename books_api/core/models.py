from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=255)
    edition = models.CharField(max_length=255, null=True)
    publication_year = models.PositiveSmallIntegerField(blank=True, null=True)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name
