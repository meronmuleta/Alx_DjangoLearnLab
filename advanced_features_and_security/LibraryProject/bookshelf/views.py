from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import HttpResponse
from .forms import ExampleForm
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

# View to display books, requires 'can_view' permission
@login_required
@permission_required('books.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# View to create a book, requires 'can_create' permission
@login_required
@permission_required('books.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Book created successfully.")
            return redirect('create_book')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})

# View to edit a book, requires 'can_edit' permission
@login_required
@permission_required('books.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, "Book updated successfully.")
            return redirect('edit_book', book_id=book_id)
    else:
        form = ExampleForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form': form, 'book': book})

# View to delete a book, requires 'can_delete' permission
@login_required
@permission_required('books.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

