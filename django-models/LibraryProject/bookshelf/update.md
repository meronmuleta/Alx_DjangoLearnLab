command:

from bookshelf.models import Book
book = Book.objects.get(id=1)
book.title = "Nineteen Eighty-Four"
book.save()

 output:

<QuerySet [<Book: Nineteen Eighty-Four by George Orwell (1949)>]>
