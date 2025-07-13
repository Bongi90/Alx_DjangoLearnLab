book1 = Book.objects.get(title="Nineteen Eighty-Four")
book1.delete()
print(Book.objects.all())
