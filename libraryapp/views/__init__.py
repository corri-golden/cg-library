from .books.list import book_list  #function of booklist.  This function is now called a view since it will handle HTTP requests
from .home import home
from .auth.logout import logout_user
from .librarians.list import librarian_list
from .libraries.list import library_list
from .books.form import book_form
from .libraries.form import library_form