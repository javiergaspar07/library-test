"""Circles API Views"""

# Django REST Framework
from rest_framework import viewsets, mixins, views
from rest_framework.response import Response

# Filters
import django_filters

# Models
from books.models import Book

# Serializers
from books.serializers import BookSerializer

# Utils
from utilities.functions.charge_books import charge_books


class AddBooks(views.APIView):
    def get(self, *args, **kwargs):
        #try:
        charge_books()
        body = 'Books charged successfully'
        status_code = 201
        """except:
            status_code = 400
            body = 'Books charge failed'"""
        
        return Response(body, status=status_code)
    
    
class BooksViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    """Circle view set."""
    
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'title'
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]   
    filter_fields = ('author')