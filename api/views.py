from django.contrib.auth.models import User
from django.http import request
from rest_framework.permissions import IsAuthenticated

from rest_framework import viewsets

from books.models import BookReview
from api.serializers import BookReviewSerializer, UserUpdateSerializer, UserRegistrationSerializer, \
UserLoginSerializer
from users.forms import UserUpdateForm
from users.forms import UserCreateForm
from django.contrib.auth import logout

from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import CustomUser


class BookReviewsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by('-created_at')
    lookup_field = 'id'


class RegistrationAPIView(APIView):
    def post(self, request):
        create_form = UserCreateForm(data=request.data)

        if create_form.is_valid():
            create_form.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(create_form.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request):
        login_form = AuthenticationForm(data=request.data)
        serializer = UserLoginSerializer(data=request.data)

        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)


class ProfileUpdateViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserUpdateSerializer
    queryset = CustomUser.objects.all()

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_serializer_class(self):
        return UserUpdateForm

# class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all()
#     lookup_field = 'id'
#
#     # def get(self, request, id):
#     #     book_review = BookReview.objects.get(id=id)
#     #
#     #     serializer = BookReviewSerializer(book_review)
#     #
#     #     return Response(data=serializer.data)
#     #
#     # def delete(self, request, id):
#     #     book_review = BookReview.objects.get(id=id)
#     #     book_review.delete()
#     #
#     #     return Response(status=status.HTTP_204_NO_CONTENT)
#     #
#     # def put(self, request, id):
#     #     book_review = BookReview.objects.get(id=id)
#     #     serializer = BookReviewSerializer(instance=book_review, data=request.data)
#     #
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     #
#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     #
#     # def patch(self, request, id):
#     #     book_review = BookReview.objects.get(id=id)
#     #     serializer = BookReviewSerializer(instance=book_review, data=request.data, partial=True)
#     #
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(data=serializer.data, status=status.HTTP_200_OK)
#     #
#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BookReviewsApiView(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticated]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all().order_by('-created_at')
#
#     # def get(self, request):
#     #     book_reviews = BookReview.objects.all().order_by('-created_at')
#     #
#     #     paginator = PageNumberPagination()
#     #     page_obj = paginator.paginate_queryset(book_reviews, request)
#     #
#     #     serializer = BookReviewSerializer(page_obj, many=True)
#     #     return paginator.get_paginated_response(serializer.data)
#     #
#     # def post(self, request):
#     #     serializer = BookReviewSerializer(data=request.data)
#     #
#     #     if serializer.is_valid():
#     #         serializer.save()
#     #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
#     #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
