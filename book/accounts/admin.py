from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Extend UserAdmin for CustomUser
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('birth_year', 'address', 'public_visibility')}),  # Add custom fields here
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('birth_year', 'address', 'public_visibility')}),  # Add custom fields here
    )

        
    # Specify the list of fields to display in the admin list view
    list_display = ['username', 'email', 'first_name', 'last_name', 'birth_year', 'address', 'public_visibility']
    search_fields = ['username', 'email', 'first_name', 'last_name']

admin.site.register(CustomUser, CustomUserAdmin)

