"""Circles API Views"""

# Django REST Framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Filters
import django_filters

# Models
from books.models import Book

# Serializers
from books.serializers import BookSerializer

# Utils
from utilities.functions.charge_books import charge_books
    
    
class BooksViewSet(viewsets.ModelViewSet):
    """Books view set."""
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]   
    filter_fields = ('author, title')

    def create(self, request, *args, **kwargs):
        """
        Manage Books creation process.
        """
        try:
            books_data = charge_books()
        except Exception as e:
            return Response(e.__str__(), status=status.HTTP_400_BAD_REQUEST)

        response = {"detail": f"{len(books_data)} Books successfully charged."}
        return Response(response, status=status.HTTP_201_CREATED)