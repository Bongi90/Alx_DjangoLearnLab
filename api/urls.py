from django.urls import path
from .views import (
    AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView,
    BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('authors/', AuthorListCreateAPIView.as_view(), name='authors-list'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='authors-detail'),
    path('books/', BookListCreateAPIView.as_view(), name='books-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='books-detail'),
]

