from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser,UploadedFiles

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

class UploadedFilesAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_description', 'visibility', 'cost', 'year_of_published', 'file_upload')  # Add the fields you want to display
    search_fields = ('book_title','book_description', 'visibility', 'cost', 'year_of_published', 'file_upload')  # Optional: Enable searching by book title

admin.site.register(UploadedFiles)

