from django.urls import path  #django package
from .views import *
from django.urls import include, path
from django.urls import path

#This file will define all of the URLs that your library application will respond to.

app_name = "libraryapp"  #name of the app. this is there so we can have multiple apps.  Like account.

urlpatterns = [
    path('', home, name='home'),
    path('books/', book_list, name='books'),      #first is taco for direction, view, name for reverse
    path('librarians/', librarian_list, name='librarians'),
    path('libraries/', library_list, name='libraries'),
    path('accounts/', include('django.contrib.auth.urls')),  #for built in login and logout
    path('logout/', logout_user, name='logout'),  #logout path
    path('book/form', book_form, name='book_form'),
    path('library/form', library_form, name='library_form'),
    path('books/<int:book_id>/', book_details, name='book'),  #The <int:book_id> part of that URL pattern is used to capture any integer that is the route parameter, and stores that number in the book_id variable.
    path('books/<int:book_id>/', book_details, name='book'),
    path('libraries/<int:library_id>/', library_details, name='library'),
]