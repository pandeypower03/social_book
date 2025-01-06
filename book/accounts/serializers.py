from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UploadedFiles 
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # ← Starts when RegisterUser API receives data
    password = serializers.CharField(
        write_only=True, # Processes password field
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):  # After validation
        return User.objects.create_user(**validated_data) # ← Ends by creating user
    
# Add FileSerializer
class FileSerializer(serializers.ModelSerializer):# ← Starts when UserFilesView processes files
    class Meta:
        model = UploadedFiles
        fields = ['id', 'book_title', 'book_description', 'visibility', 
                 'cost', 'year_of_published', 'file_upload']# Specifies which fields to convert
         # ← Ends by converting model data to JSON