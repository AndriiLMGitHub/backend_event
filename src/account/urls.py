from django.urls import path
from . import views
from .api import upload_avatar_images, get_avatar_images


urlpatterns = [
    path('profile/', views.ProfileAPIView.as_view()),
    path('profile/<str:pk>/', views.ProfileDetailAPIView.as_view()),

    path('profile/image/upload/', views.UserProfileImageUploadAPIView.as_view()),
    path('profile/images/', views.UserProfileImagesAPIView.as_view()),
]