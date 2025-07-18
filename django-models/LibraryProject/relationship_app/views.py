from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library, Author 

def list_books(request):
    """
    Retrieves all books from the database and renders them in a list_books.html template.
    """
    books = Book.objects.all().order_by('title') 
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

class LibraryDetailView(DetailView):
    """
    Displays details for a specific Library instance, including all books associated with it.
    Uses Django's DetailView generic class-based view.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' 

    def get_context_data(self, **kwargs):
        """
        Adds extra context to the template, if needed.
        For DetailView, the object itself (library) is automatically passed.
        """
        context = super().get_context_data(**kwargs)
        return context



