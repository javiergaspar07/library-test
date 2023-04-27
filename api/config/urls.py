"""
URL configuration for library API project.
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # Books
    path('books/', include(('api.books.urls', 'books'), namespace='books')),
]
