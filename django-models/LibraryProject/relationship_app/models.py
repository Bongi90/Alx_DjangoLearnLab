# relationship_app/models.py

from django.db import models

# Author Model: A simple model for authors.
# This model will be referenced by the Book model using a ForeignKey.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book Model: Represents a book with a title and an author.
# It has a ForeignKey to Author, indicating that each book has one author,
# but an author can have many books (one-to-many relationship).
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    # on_delete=models.CASCADE means if an Author is deleted, all their Books are also deleted.
    # related_name='books' allows us to access books from an Author instance (e.g., author.books.all()).

    def __str__(self):
        return self.title

# Library Model: Represents a library that can hold multiple books.
# It has a ManyToManyField to Book, meaning a library can have many books,
# and a book can belong to many libraries.
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='libraries')
    # related_name='libraries' allows us to access libraries from a Book instance (e.g., book.libraries.all()).

    def __str__(self):
        return self.name

# Librarian Model: Represents a librarian who is uniquely associated with one library.
# It has a OneToOneField to Library, meaning each librarian is linked to exactly one library,
# and each library has exactly one librarian (one-to-one relationship).
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')
    # on_delete=models.CASCADE means if a Library is deleted, its associated Librarian is also deleted.
    # related_name='librarian' allows us to access the librarian from a Library instance (e.g., library.librarian).

    def __str__(self):
        return self.name
