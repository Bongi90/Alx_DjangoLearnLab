from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Author, Genre # Ensure all necessary models are imported
from .forms import BookForm # Assuming you have a BookForm defined for creation/editing


@login_required
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# --- Create View (can_create_book) ---
@login_required
@permission_required('bookshelf.can_create_book', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list') # Redirect to book list after creation
    else:
        form = BookForm()
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Create'})


@login_required
@permission_required('bookshelf.can_edit_book', raise_exception=True)
def book_edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list') 
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form, 'action': 'Edit'})


@login_required
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list') 
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})

