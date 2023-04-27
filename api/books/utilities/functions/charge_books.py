# Third Party
import pandas as pd

# Local
from api.books.serializers import BookSerializer
from api.books.models import Book

def charge_books():
    """
    Create Book objects from books.csv dataset.
    """
    # Checking if books already charged
    books = Book.objects.count()
    if books:
        raise Exception({"detail": "Books already charged."})
    
    # Reading csv file to charge books
    df = pd.read_csv(
        "api/books/utilities/datasets/books.csv",
        encoding="ISO-8859-1",
        sep=";",
        on_bad_lines="skip"
    )
    equivalent_columns = ['isbn', 'title', 'author', 'year_of_publication',
                          'publisher', 'image_URL_S','image_URL_M', 'image_URL_L']
    cleaned_df = df.where(pd.notnull(df), None)

    # Data validation and books creation
    books_data = []
    for book in cleaned_df.values.tolist():
        book_dict = dict(zip(equivalent_columns, book))
        book_dict['isbn'] = book_dict.get('isbn').upper()
        serializer = BookSerializer(data=book_dict)
        if not serializer.is_valid():
            continue
        serializer.save()
        books_data.append(serializer.data)
    
    return books_data