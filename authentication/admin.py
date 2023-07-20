from django.contrib import admin

# Register your models here.
# myapp/admin.py

from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('is_renter',)

admin.site.register(User, CustomUserAdmin)

