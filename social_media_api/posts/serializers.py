from rest_framework import serializers
from .models import Post, Comment
from accounts.serializers import UserRegistrationSerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserRegistrationSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    author = UserRegistrationSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'updated_at']