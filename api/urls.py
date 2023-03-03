from django.urls import path

from api.views import BookReviewDetailAPIView, BookReviewsApiView

app_name = "api"
urlpatterns = [
    path("reviews/", BookReviewsApiView.as_view(), name="review-list"),
    path("reviews/<int:id>/", BookReviewDetailAPIView.as_view(), name="review-detail"),
]