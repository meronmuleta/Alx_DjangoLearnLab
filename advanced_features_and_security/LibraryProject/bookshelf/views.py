from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponse
from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# View to display books, requires 'can_view' permission
@login_required
@permission_required('books.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

# View to create a book, requires 'can_create' permission
@login_required
@permission_required('books.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully.")
            return redirect('bookshelf/view_books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})

# View to edit a book, requires 'can_edit' permission
@login_required
@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect('bookshelf/view_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

# View to delete a book, requires 'can_delete' permission
@login_required
@permission_required('books.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('bookshelf/view_books')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

