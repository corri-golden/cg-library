import sqlite3
from django.shortcuts import render
from libraryapp.models import Librarian
from ..connection import Connection
from libraryapp.models import Library

#@login_required
def library_list(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # db_cursor.execute("""
        # select
        #     l.id,
        #     l.title,
        #     l.address,
        # from libraryapp_library l
        # """)

        db_cursor.execute("""
            select
                l.id,
                l.title,
                l.address
            from libraryapp_library l
        """)

        all_libraries = []
        dataset = db_cursor.fetchall()
 
        for row in dataset:
            library = Library()
            library.id = row["id"]
            library.title = row["title"]
            library.address = row["address"]

            all_libraries.append(library)

    template_name = 'libraries/list.html'

    context = {
        'all_libraries': all_libraries
    }

    return render(request, template_name, context)