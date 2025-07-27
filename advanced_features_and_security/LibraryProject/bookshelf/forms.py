from django import forms
from .models import Book 


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'isbn', 'borrowed_by', 'return_date']


class ExampleForm(forms.Form):
    """
    A simple example form for demonstrating CSRF protection.
    """
    name = forms.CharField(max_length=100, label="Your Name")
    message = forms.CharField(widget=forms.Textarea, label="Your Message")