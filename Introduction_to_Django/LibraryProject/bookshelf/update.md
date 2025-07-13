## Python Command:
```python
from bookshelf.models import Book # Only need this if you restart the shell
book1 = Book.objects.get(title="1984") # Retrieve the book (assuming it exists and hasn't been deleted yet)
book1.title = "Nineteen Eighty-Four"
book1.save()
print(book1.title) # Confirm the updated title
