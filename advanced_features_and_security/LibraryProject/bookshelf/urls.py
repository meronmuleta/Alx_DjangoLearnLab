from django.urls import path
from .views import book_list, create_book, edit_book, delete_book

urlpatterns = [
    path('', book_list, name='book_list'),
    path('create/', create_book, name='create_book'),
    path('<int:book_id>/edit/', edit_book, name='edit_book'),
    path('<int:book_id>/delete/', delete_book, name='delete_book'),
]

