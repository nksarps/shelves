from .models import Book
from rest_framework import serializers


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'description', 'author', 'publication_date', 'genre', 'user', 'created_at']

        read_only_fields = ['user']