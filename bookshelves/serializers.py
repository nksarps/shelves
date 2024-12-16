from .models import Bookshelf
from rest_framework import serializers


class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ['id', 'name', 'description', 'user', 'created_at', 'updated_at']

        read_only_fields = ['id', 'user']