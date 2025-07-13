## Python Command:
```python
from bookshelf.models import Book # Only need this if you restart the shell
book1 = Book.objects.get(title="Nineteen Eighty-Four") # Get the book by its updated title
book1.delete()
print(Book.objects.all()) # Confirm deletion by showing all books (should be empty)
