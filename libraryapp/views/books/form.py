import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required   #You are going to modify your application so that books, libraries, and librarians can only be viewed if the user is authenticated
from libraryapp.models import Book
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection


def get_libraries(): # gets libraries for form dropdown
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Library)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.title,
            l.address
        from libraryapp_library l
        """)

        return db_cursor.fetchall()

@login_required
def book_form(request):
    if request.method == 'GET':
        libraries = get_libraries()
        template = 'books/form.html'
        context = {
            'all_libraries': libraries
        }

        return render(request, template, context) # renders the book form and passes the libraries, template, and context to it

