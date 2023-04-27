# Third Party
import pandas as pd

# Local
from books.serializers import BookSerializer
from books.models import Book

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
        "utilities/datasets/books.csv",
        encoding="ISO-8859-1",
        sep=";",
        on_bad_lines="skip"
    )
    equivalent_columns = ['isbn', 'title', 'author', 'year_of_publication',
                          'publisher', 'image_URL_S','image_URL_M', 'image_URL_L']
    cleaned_df = df.where(pd.notnull(df), None)

    # Data validation
    books_serializers = []
    for book in cleaned_df.values.tolist():
        book_dict = dict(zip(equivalent_columns, book))
        book_dict['isbn'] = book_dict.get('isbn').upper()
        serializer = BookSerializer(data=book_dict)
        if not serializer.is_valid():
            continue
        books_serializers.append(serializer)
    
    # Books creation
    books_data = []
    for book in books_serializers:
        book.save()
        books_data.append(book.data)
    
    return books_data