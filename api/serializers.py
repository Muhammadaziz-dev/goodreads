from rest_framework import serializers
from rest_framework.views import APIView

from books.models import Book, BookReview
from users.models import CustomUser


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'isbn')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'first_name', 'last_name', 'email', 'username')


class BookReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    book = BookSerializer()

    class Meta:
        model = BookReview
        fields = ('id', 'stars_given', 'comment', 'book', 'user')


