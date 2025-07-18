import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_name = "John Doe"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print("Books by", author_name, ":", [book.title for book in books_by_author])

library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print("Books in", library_name, ":", [book.title for book in books_in_library])

librarian = Librarian.objects.get(library=library)
print(f"Librarian for {library.name}: {librarian.name}")

