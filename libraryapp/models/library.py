from django.db import models  #This import is needed for Python classes that are modeling a database table

class Library (models.Model):

    title = models.CharField(max_length=50)  ## properties for the class
    address = models.CharField(max_length=50)  ## properties for the class

    class Meta:
        verbose_name =("library")
        verbose_name_plural = ("libraries")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
