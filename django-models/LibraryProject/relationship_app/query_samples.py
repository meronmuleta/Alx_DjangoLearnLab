from library.models import Book
books = Book.objects.select_related("author")
for book in books:
    print(f"Title: {book.title}, Author: {book.author.name}")

from library.models import Library
libraries = Library.objects.prefetch_related('books')
for library in libraries:
      print(f"Library: {library.name}")
      books_in_library = library.books.all()
      for book in books_in_library:
          print(f" - {book.title}")


from library.models import Librarian
librarians = Librarian.objects.select_related('library')
for librarian in librarians:
    print(f"Librarian: {librarian.name}, Library: {librarian.library.name}")
