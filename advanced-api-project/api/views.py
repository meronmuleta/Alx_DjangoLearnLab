from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List view for retrieving all books
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Detail view for retrieving a single book by ID
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Create view for adding a new book
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]  # Restricting to authenticated users

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
    permission_classes = [permissions.IsAuthenticated]

# Delete view for removing a book
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

