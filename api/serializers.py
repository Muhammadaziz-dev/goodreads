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
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)
    book_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = BookReview
        fields = ('id', 'stars_given', 'comment', 'book', 'user', 'user_id', 'book_id')


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_picture', 'phone_number']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    username_or_email_or_phone = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(write_only=True, required=True)