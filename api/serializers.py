from rest_framework import serializers
from .models import Author, Book
import datetime

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    - serializes all Book fields (id, title, publication_year, author).
    - includes validation to ensure publication_year is not in the future.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class NestedBookSerializer(serializers.ModelSerializer):
    """
    Nested representation of Book used under AuthorSerializer.
    Excludes the 'author' field to avoid redundancy.
    This is used for (de)serializing nested book objects in Author endpoints.
    """
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year']


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model that includes nested books.

    - 'books' is a nested list using NestedBookSerializer.
    - Supports writable nested create and update:
        - On create, nested books (if provided) are validated using BookSerializer and then created.
        - On update, if 'books' is provided it will replace the Author's books (simple strategy).
    """
    books = NestedBookSerializer(many=True, required=False)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

    def create(self, validated_data):
        books_data = validated_data.pop('books', [])
        author = Author.objects.create(**validated_data)

        # Validate each nested book with the full BookSerializer (so validation rules apply)
        for book_data in books_data:
            # attach author id so BookSerializer can resolve relation and perform validation
            payload = {**book_data, 'author': author.id}
            book_serializer = BookSerializer(data=payload)
            book_serializer.is_valid(raise_exception=True)
            book_serializer.save()

        return author

    def update(self, instance, validated_data):
        books_data = validated_data.pop('books', None)
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        if books_data is not None:
            # Replace existing books with provided list (simple strategy).
            instance.books.all().delete()
            for book_data in books_data:
                payload = {**book_data, 'author': instance.id}
                book_serializer = BookSerializer(data=payload)
                book_serializer.is_valid(raise_exception=True)
                book_serializer.save()

        return instance
