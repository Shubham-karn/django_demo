# authentication/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    # Add the custom field to the "Personal Info" section
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('phone','isRenter','profilePicture','occupation')}),
    )

# Register the CustomUser model with the CustomUserAdmin class
admin.site.register(User, CustomUserAdmin)
