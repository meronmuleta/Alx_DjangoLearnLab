from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
    def validate_publication_year(self,data):
        if data > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return data
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True) #Nested serializer
    class Meta:
        model=Author
        fields = ['id','name','books']
