def charge_books():
    import csv
    from books.models import Book
    headers = ['isbn', 'title', 'author',
               'year_of_publication', 'publisher', 'image_URL_S',
               'image_URL_M', 'image_URL_L']
    books = []
    with open("utilities/datasets/books.csv", 'r') as file:
        csvreader = csv.reader(file)
        for count, row in enumerate(csvreader):
            if count == 0:
                continue
            
            try:
                values = row[0].split(';')
                cleaned_values = [value.replace('"','') for value in values]
                book_data = dict(zip(headers, cleaned_values))
                Book.objects.create(**book_data)
            except:
                pass
    
    return "Books created."