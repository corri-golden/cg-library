from django.db import models #This import is needed for Python classes that are modeling a database table
from .library import Library  ## import for the foreign keys
from .librarian import Librarian  ## import for the foreign keys


class Book (models.Model):

    title = models.CharField(max_length=50)  ## properties for the class
    ISBN = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year_published = models.CharField(max_length=50)
    location = models.ForeignKey(Library, on_delete=models.CASCADE)  ## foreign keys
    librarian = models.ForeignKey(Librarian, on_delete=models.CASCADE)  ## foreign keys

    class Meta:
        verbose_name = ("Book")
        verbose_name_plural = ("Books")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Book_detail", kwargs={"pk": self.pk})
