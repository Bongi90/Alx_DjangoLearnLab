from django.db import models

class Author(models.Model):
    """
    Represents an author.

    Fields:
        - name: the full name of the author (string)
    Relationship:
        - One Author can have many Books (reverse name: 'books').
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Represents a book.

    Fields:
        - title: book title
        - publication_year: integer year when the book was published
        - author: ForeignKey to Author; establishes a one-to-many relationship
                  (Author -> Book). `related_name='books'` allows `author.books.all()`.
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"