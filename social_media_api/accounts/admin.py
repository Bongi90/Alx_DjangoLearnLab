from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Profile", {"fields": ("bio", "profile_picture", "following")}),
    )
    filter_horizontal = ("groups", "user_permissions", "following")
    list_display = ("username", "email", "is_staff", "followers_count", "following_count")

