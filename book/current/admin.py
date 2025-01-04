from django.contrib import admin


from .models import Uploaded
class UploadedFilesAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_description', 'visibility', 'cost', 'year_of_published', )  # Add the fields you want to display
    search_fields = ('book_title','book_description', 'visibility', 'cost', 'year_of_published', )  # Optional: Enable searching by book title

admin.site.register(Uploaded,UploadedFilesAdmin)
# Register your models here.
