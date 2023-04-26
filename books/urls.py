"""Books Auth URLs"""

# Django
from django.urls import path, include

# Views
from books.views import BooksViewSet, AddBooks

# Django REST Framework
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', BooksViewSet, basename='books')

urlpatterns = [
    path('', include(router.urls)),
]