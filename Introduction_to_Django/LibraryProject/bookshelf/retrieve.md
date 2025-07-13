book1 = Book.objects.get(title="1984") # Or use pk=1 if you know its primary key
print(book1.title)
print(book1.author)
print(book1.publication_year)
