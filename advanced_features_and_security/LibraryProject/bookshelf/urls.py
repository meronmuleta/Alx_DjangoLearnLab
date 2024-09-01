from django.urls import path
from .views import view_books, create_book, edit_book, delete_book

urlpatterns = [
    path('', view_books, name='view_books'),
    path('create/', create_book, name='create_book'),
    path('<int:book_id>/edit/', edit_book, name='edit_book'),
    path('<int:book_id>/delete/', delete_book, name='delete_book'),
]

