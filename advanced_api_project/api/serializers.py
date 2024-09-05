from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

class AuthorSerializer(serializers.ModelSerializer):
    """
    The AuthorSerializer serializes the name field of the Author model.
    It includes a nested BookSerializer to serialize the related books dynamically.
    """
    
    books = BookSerializer(many=True, read_only=True)

    class Meta:
       model = Author
       fields =  ['name', 'books']

class BookSerializer(serializers.ModelSerializer):
    """
    The BookSerializer serializes all fields of the Book model.
    It includes custom validation to ensure the publication year is not in the future.
    """
    class Meta:
        model = Book
        fields = 'id', 'title', 'author', 'publication_year'

    def validate_publication_year(self, value):
        """
        Custom validator to ensure the publication year is not in the future.
        """
        create_year = datetime.now().year
        if value > create_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value