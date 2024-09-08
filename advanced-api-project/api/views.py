from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated  # Import permissions
from .models import Book
from .serializers import BookSerializer

# List view for retrieving all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read access for everyone, write access for authenticated users

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Setting up filters
    filterset_fields = ['title', 'author__name', 'publication_year']  # Allows filtering by these fields

    # Setting up search
    search_fields = ['title', 'author__name']  # Allows searching by title and author's name

    # Setting up ordering
    ordering_fields = ['title', 'publication_year']  # Allows ordering by title and publication_year

# Detail view for retrieving a single book by ID
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read access for everyone, write access for authenticated users

# Create view for adding a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restricting to authenticated users

    def perform_create(self, serializer):
        # Example: Prevent creating a book with the same title and publication year
        title = serializer.validated_data.get('title')
        publication_year = serializer.validated_data.get('publication_year')
        if Book.objects.filter(title=title, publication_year=publication_year).exists():
            raise serializers.ValidationError("A book with this title and publication year already exists.")
        serializer.save()

# Update view for modifying an existing book
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# Delete view for removing a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

