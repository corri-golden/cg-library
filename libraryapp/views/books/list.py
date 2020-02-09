import sqlite3
from django.shortcuts import render
from libraryapp.models import Book
from ..connection import Connection
from libraryapp.models import model_factory
from django.contrib.auth.decorators import login_required

#Note that the row factory being used for this connection to the database uses the built-in sqlite3.Row method. This allows developers to access columns in each row in the dataset by the column name instead of by index in the tuple.

#book_list function handles http request

@login_required   #after putting login required at form.py
def book_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            
            conn.row_factory = model_factory(Book)
            
            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                b.id,
                b.title,
                b.isbn,
                b.author,
                b.year_published,
                b.librarian_id,
                b.location_id
            from libraryapp_book b
            """)

            all_books = db_cursor.fetchall()

            # for row in dataset:
            #     book = Book()
            #     book.id = row['id']
            #     book.title = row['title']
            #     book.isbn = row['isbn']
            #     book.author = row['author']
            #     book.year_published = row['year_published']
            #     book.librarian_id = row['librarian_id']
            #     book.location_id = row['location_id']

            #     all_books.append(book)

        template = 'books/list.html'
        context = {
            'all_books': all_books
        }

        return render(request, template, context)


#When a view wants to generate some HTML representations of data, it needs to specify a template to use. Above, the template variable is holding the path and filename of the template you just created.

#Then the render() method is invoked. That method takes the HTTP request as the first argument, the template to be used as the second argument, and then a dictionary containing the data to be used in the template.