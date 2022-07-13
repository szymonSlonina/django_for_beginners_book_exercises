from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.
# update admin to utilize CustomUser model
# update UserAdmin with CustomUser data.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "is_staff"
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),) # fields used in editing
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),) # fields used when creating

admin.site.register(CustomUser, CustomUserAdmin)