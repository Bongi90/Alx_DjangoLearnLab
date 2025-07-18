# relationship_app/query_samples.py

# To run this script:
# 1. Ensure you are in the 'django-models' directory.
# 2. Run: python manage.py shell
# 3. Inside the shell, run: exec(open('relationship_app/query_samples.py').read())

import os
import django

# Configure Django settings to allow running this script independently
# This is crucial for the script to access your Django models
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

# Import your models
from relationship_app.models import Author, Book, Library, Librarian

def run_sample_queries():
    print("--- Running Sample Queries ---")

    # Clean up existing data for a fresh run (optional)
    # This is useful for testing, but be careful in production!
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()
    print("Cleaned up existing data.")

    # --- 1. Create Sample Data ---
    print("\n--- Creating Sample Data ---")

    # Authors
    author1 = Author.objects.create(name="Jane Austen")
    author2 = Author.objects.create(name="George Orwell")
    author3 = Author.objects.create(name="Agatha Christie")
    print(f"Created Authors: {author1.name}, {author2.name}, {author3.name}")

    # Books (ForeignKey to Author)
    book1 = Book.objects.create(title="Pride and Prejudice", author=author1)
    book2 = Book.objects.create(title="1984", author=author2)
    book3 = Book.objects.create(title="Animal Farm", author=author2)
    book4 = Book.objects.create(title="Murder on the Orient Express", author=author3)
    book5 = Book.objects.create(title="Emma", author=author1)
    print(f"Created Books: {book1.title}, {book2.title}, {book3.title}, {book4.title}, {book5.title}")

    # Libraries (ManyToMany to Book)
    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="Community Reading Hub")
    print(f"Created Libraries: {library1.name}, {library2.name}")

    # Add books to libraries
    library1.books.add(book1, book2, book4) # Central Library has Pride and Prejudice, 1984, Murder on the Orient Express
    library2.books.add(book2, book3, book5) # Community Reading Hub has 1984, Animal Farm, Emma
    print("Added books to libraries.")

    # Librarians (OneToOneField to Library)
    librarian1 = Librarian.objects.create(name="Alice Smith", library=library1)
    librarian2 = Librarian.objects.create(name="Bob Johnson", library=library2)
    print(f"Created Librarians: {librarian1.name}, {librarian2.name}")


    # --- 2. Implement Sample Queries ---
    print("\n--- Running Queries ---")

    # Query 1: Query all books by a specific author (ForeignKey relationship)
    print("\n--- Query: Books by Jane Austen ---")
    jane_austen_books = Book.objects.filter(author=author1) # or author=Author.objects.get(name="Jane Austen")
    for book in jane_austen_books:
        print(f"  - {book.title} by {book.author.name}")

    # Using reverse relationship (related_name='books' on Author's ForeignKey)
    print("\n--- Query: Books by George Orwell (using related_name) ---")
    george_orwell = Author.objects.get(name="George Orwell")
    for book in george_orwell.books.all(): # Accessing books via author.books.all()
        print(f"  - {book.title}")

    # Query 2: List all books in a library (ManyToManyField relationship)
    print("\n--- Query: Books in Central Library ---")
    central_library = Library.objects.get(name="Central Library")
    for book in central_library.books.all():
        print(f"  - {book.title}")

    print("\n--- Query: Books in Community Reading Hub ---")
    community_library = Library.objects.get(name="Community Reading Hub")
    for book in community_library.books.all():
        print(f"  - {book.title}")

    # Query 3: Retrieve the librarian for a library (OneToOneField relationship)
    print("\n--- Query: Librarian for Central Library ---")
    try:
        central_library_librarian = central_library.librarian # Accessing librarian via library.librarian
        print(f"  - Librarian for Central Library: {central_library_librarian.name}")
    except Librarian.DoesNotExist:
        print("  - No librarian found for Central Library.")

    print("\n--- Query: Librarian for Community Reading Hub ---")
    try:
        community_library_librarian = community_library.librarian
        print(f"  - Librarian for Community Reading Hub: {community_library_librarian.name}")
    except Librarian.DoesNotExist:
        print("  - No librarian found for Community Reading Hub.")

    # Reverse lookup from Librarian to Library
    print("\n--- Query: Library for Alice Smith ---")
    alice_smith = Librarian.objects.get(name="Alice Smith")
    print(f"  - Library for Alice Smith: {alice_smith.library.name}")

    print("\n--- Sample Queries Completed ---")

# Execute the function when the script is run
if __name__ == "__main__":
    run_sample_queries()
