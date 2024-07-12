from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.conf import settings


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("Email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


# Profile Model
class Profile(models.Model):
    CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    # sex = models.CharField(max_length=20, choices=CHOICES, null=True, blank=True, default='Male')
    name = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f'User profile - {self.user}'

    class Meta:
        verbose_name = "User Profile"


# User Profile Avatar Model
class UserProfileImage(models.Model):
    user_profile_id = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='profile_images'
    )
    avatar = models.FileField(
        upload_to='user/avatars/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Avatar - {self.user_profile_id.id}'

    class Meta:
        verbose_name = "User Profile Image"


# Signal to create Profile and Host models on user creation
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
