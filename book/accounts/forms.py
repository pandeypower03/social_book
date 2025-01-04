from django import forms
from .models import UploadedFiles

class UploadedFilesForm(forms.ModelForm):
    class Meta:
        model = UploadedFiles
        fields = ['book_title', 'book_description', 'visibility', 'cost', 'year_of_published', 'file_upload']
