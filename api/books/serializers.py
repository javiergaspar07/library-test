# REST Framework
from rest_framework import serializers

# Local
from api.books.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        """Meta class"""
        
        model = Book
        fields = '__all__'