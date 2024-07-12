from rest_framework import generics
from rest_framework import permissions
from rest_framework import parsers
from .serializers import UserProfileImageSerializer, ProfileSerializer
from .models import Profile, UserProfileImage


class ProfileAPIView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class ProfileDetailAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [permissions.IsAuthenticated]


class UserProfileImageUploadAPIView(generics.CreateAPIView):
    serializer_class = UserProfileImageSerializer
    queryset = UserProfileImage.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [
        parsers.FileUploadParser,
        parsers.FormParser,
        parsers.MultiPartParser
    ]


class UserProfileImagesAPIView(generics.ListAPIView):
    serializer_class = UserProfileImageSerializer
    queryset = UserProfileImage.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    # parser_classes = [
    #     parsers.FileUploadParser,
    #     parsers.FormParser,
    #     parsers.MultiPartParser
    # ]
