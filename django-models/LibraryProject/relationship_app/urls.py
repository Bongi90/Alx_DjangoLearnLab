from django.urls import path
from . import views # Import views from the current app
from django.contrib.auth import views as auth_views # NEW: Import Django's built-in auth views

app_name = 'relationship_app' # Namespace for this app's URLs

urlpatterns = [

    path('books/', views.list_books, name='list_books'),

    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    path('register/', views.register, name='register'),

    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logged_out.html', next_page='relationship_app:list_books'), name='logout'),
]
