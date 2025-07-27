from django.db import models
from django.conf import settings 

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)

    borrowed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    return_date = models.DateField(null=True, blank=True)

    class Meta:

        permissions = [
            ("can_view", "Can view book details"),
            ("can_create", "Can create new books"),
            ("can_edit", "Can edit existing books"),
            ("can_delete", "Can delete books"),
        ]
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title
