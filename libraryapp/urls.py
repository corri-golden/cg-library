from django.urls import path  #django package
from .views import *
from django.urls import include, path

#This file will define all of the URLs that your library application will respond to.

app_name = "libraryapp"

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),
    path('librarians/', librarian_list, name='librarians'),
    path('libraries/', library_list, name='libraries'),
    path('accounts/', include('django.contrib.auth.urls')),  #for built in login and logout
    path('logout/', logout_user, name='logout'),  #logout path
    path('book/form', book_form, name='book_form'),
    # path('library/form', library_form, name='library_form'),
]