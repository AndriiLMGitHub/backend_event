from django.contrib import admin
from .models import CustomUser, Profile, UserProfileImage


class CustomUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(UserProfileImage)
