# Built-in
from datetime import datetime

# Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator


ISBN_REGEX = r'\d{10}$'
CURRENT_YEAR = datetime.now().year

class Book(models.Model):
    isbn = models.CharField(
        validators=[RegexValidator(
            regex=ISBN_REGEX,
            message="ISBN must be entered in the format: 9999999999."
        )],
        max_length=10
    )
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year_of_publication = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(CURRENT_YEAR)
        ]
    )
    publisher = models.CharField(max_length=200)
    image_URL_S = models.URLField()
    image_URL_M = models.URLField()
    image_URL_L = models.URLField()