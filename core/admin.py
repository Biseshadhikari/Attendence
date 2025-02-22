from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "is_active", "is_superuser", "usertype")
    list_filter = ("is_staff", "is_active", "is_superuser", "usertype")
    search_fields = ("username", "email", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": ("username", "password", "usertype")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "password1", "password2", 'usertype', "is_staff",
                "is_active", "is_superuser", "groups", "user_permissions"
            )}
        ),
    )
    ordering = ("username",)

admin.site.register(Attendance)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Mentor)
admin.site.register(Course)
admin.site.register(Students)
admin.site.register(Profile)
