# advanced_features_and_security/bookshelf/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author, Genre # Ensure all necessary models are imported

# IMPORTANT: You need a forms.py in your bookshelf app for the create/edit views.
# Example content for bookshelf/forms.py:
# from django import forms
# from .models import Book
# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'genre', 'publication_date', 'isbn', 'borrowed_by', 'return_date']

from .forms import BookForm # Assuming you have bookshelf/forms.py with BookForm


# --- List View: Requires 'can_view' permission ---
@login_required # User must be logged in
@permission_required('bookshelf.can_view', raise_exception=True) # Checks for the 'can_view' permission
def book_list(request):
    books = Book.objects.all()
    # You will need a template at advanced_features_and_security/bookshelf/templates/bookshelf/book_list.html
    return render(request, 'bookshelf/book_list.html', {'books': books})

# --- Create View: Requires 'can_create' permission ---
@login_required
@permission_required('bookshelf.can_create', raise_exception=True) # Checks for the 'can_create' permission
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') # Redirect to your book list URL name
    else:
        form = BookForm()
    # You will need a template at advanced_features_and_security/bookshelf/templates/bookshelf/book_form.html
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Create'})

# --- Edit View: Requires 'can_edit' permission ---
@login_required
@permission_required('bookshelf.can_edit', raise_exception=True) # Checks for the 'can_edit' permission
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list') # Redirect to your book list URL name
    else:
        form = BookForm(instance=book)
    # Uses the same form template as create
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Edit'})

# --- Delete View: Requires 'can_delete' permission ---
@login_required
@permission_required('bookshelf.can_delete', raise_exception=True) # Checks for the 'can_delete' permission
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list') # Redirect to your book list URL name
    # You will need a template at advanced_features_and_security/bookshelf/templates/bookshelf/book_confirm_delete.html
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})