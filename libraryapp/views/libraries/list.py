import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Librarian
from ..connection import Connection
from libraryapp.models import Library
from django.contrib.auth.decorators import login_required
from libraryapp.models import model_factory

#@login_required
def library_list(request):
    if request.method == 'GET':
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

        all_libraries = db_cursor.fetchall()
        # dataset = db_cursor.fetchall()
 
        # for row in dataset:
        #     library = Library()
        #     library.id = row["id"]
        #     library.title = row["title"]
        #     library.address = row["address"]

        # all_libraries.append(library)

        template_name = 'libraries/list.html'

        context = {
            'all_libraries': all_libraries
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        form_data = request.POST

        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            INSERT INTO libraryapp_library
            (
            title, address
            )
            VALUES (?, ?)
            """,
#The values thing above is quality control, protection from bad data injection.
        (form_data['title'], form_data['address']))

    return redirect(reverse('libraryapp:libraries'))
    

