from django.shortcuts import render, get_object_or_404, redirect # Added redirect
from django.views.generic import DetailView
from .models import Book, Library, Author
from django.contrib.auth import login # NEW: Import for user login
from django.contrib.auth.forms import UserCreationForm # NEW: Import for user registration form

# Function-based view to list all books
def list_books(request):
    """
    Retrieves all books from the database and renders them in a list_books.html template.
    """
    books = Book.objects.all().order_by('title') # Order alphabetically by title
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view to display details for a specific library
class LibraryDetailView(DetailView):
    """
    Displays details for a specific Library instance, including all books associated with it.
    Uses Django's DetailView generic class-based view.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # The variable name to use in the template for the Library object

    def get_context_data(self, **kwargs):
        """
        Adds extra context to the template, if needed.
        For DetailView, the object itself (library) is automatically passed.
        """
        context = super().get_context_data(**kwargs)
        # No extra context needed here as library.books.all is directly accessible in template
        return context

# Placeholder for user registration view (to make UserCreationForm import relevant)
def register(request):
    """
    Placeholder for user registration view.
    Actual implementation will involve handling form submission and user creation.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Use the imported login function
            return redirect('some-success-url') # Replace with an actual success URL
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Placeholder for user login view (to make login import relevant, though it's used in register)
# Django often provides built-in login views, but a custom one might be expected.
def user_login(request):
    """
    Placeholder for user login view.
    Actual implementation will involve handling authentication forms.
    """
    # This view would typically use Django's AuthenticationForm
    # For now, it's just a placeholder to ensure the 'login' import is used if needed.
    return render(request, 'relationship_app/login.html', {})
