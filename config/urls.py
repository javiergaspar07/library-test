"""
URL configuration for library API project.
"""
from django.contrib import admin
from django.urls import path, include

# Local
from books.views import AddBooks

urlpatterns = [
    path('admin/', admin.site.urls),

    # Books
    path('books/', include(('books.urls', 'books'), namespace='books')),

    path('add-books/', AddBooks.as_view(), name='add-books')
]
