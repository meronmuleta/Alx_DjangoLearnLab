from rest_framework import serializers
from .models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # To display the username
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments']

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)  # To display the username

    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'content', 'created_at', 'updated_at']
