from django.contrib import admin
from .models import CustomUser, UploadedFiles

# Register CustomUser with custom settings in the admin panel
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'birth_year', 'address', 'public_visibility')
    search_fields = ('username', 'email')
    list_filter = ('public_visibility',)

admin.site.register(CustomUser, CustomUserAdmin)

# Register UploadedFiles model with the admin panel
class UploadedFilesAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'user', 'visibility', 'cost', 'year_of_published', 'file_upload')
    search_fields = ('book_title', 'user__username')  # Search by book title or username
    list_filter = ('visibility', 'year_of_published')

admin.site.register(UploadedFiles, UploadedFilesAdmin)

