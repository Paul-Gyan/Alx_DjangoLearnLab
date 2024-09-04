from django.db import models

# Create your models here.
class Author(models.Model):
    """
    The Author model represents an author with a name.
    Each author can write multiple books, establishing a one-to-many relationship with the Book model.
    """
    name = models.CharField(max_length=255)

class Book(models.Model):
    """
    The Book model represents a book with a title, publication year, and an author.
    Each book is linked to a single author, establishing a foreign key relationship with the Author model.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()