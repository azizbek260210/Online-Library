from rest_framework import serializers
from main.models import User, Category, Author, Books, Review, Quotes

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'status', 'bio', 'image']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'full_name', 'image', 'bio', 'description', 'birthday', 'dead_day']

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['id', 'name', 'image', 'page', 'year', 'publisher', 'description', 'author', 'category', 'paper_book', 'price', 'audio_book', 'audio_book_file', 'electron_book', 'electron_book_file']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'book', 'user', 'mark', 'text']

class QuotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        fields = ['id', 'book', 'body']
