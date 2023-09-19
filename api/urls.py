from django.urls import path

# from api.views import BookReviewDetailAPIView, BookReviewsApiView
from rest_framework.routers import DefaultRouter
from api.views import BookReviewsViewSet, ProfileUpdateViewSet, LoginAPIView, RegistrationAPIView, LogoutAPIView

app_name = "api"
router = DefaultRouter()
router.register('reviews', BookReviewsViewSet, basename='review')
router.register(r'profile-update', ProfileUpdateViewSet, basename='profile-update')


urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login-api'),
    path('register/', RegistrationAPIView.as_view(), name='register-api'),
    path('logout/', LogoutAPIView.as_view(), name="logout-api")
]

urlpatterns += router.urls