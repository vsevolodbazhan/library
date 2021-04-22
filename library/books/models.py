from django.db import models


class Author(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)

    class Meta:
        ordering = ["name"]
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(verbose_name="Title", max_length=250)
    description = models.TextField(verbose_name="Description")
    authors = models.ManyToManyField(Author)

    class Meta:
        ordering = ["title"]
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
