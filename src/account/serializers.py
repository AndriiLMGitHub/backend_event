from rest_framework import serializers
from .models import Profile, UserProfileImage


class UserProfileImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileImage
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    profile_images = UserProfileImageSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = [
            'id',
            'name',
            'bio',
            'is_verified',
            'profile_images'
        ]
