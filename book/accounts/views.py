from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UploadedFiles
from .forms import UploadedFilesForm
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers

# Your existing views remain the same
def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = CustomUser.objects.create_user(username=username, password=password)
            return redirect('login')
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', reverse('upload_file'))
            return redirect(next_url)
        else:
            return HttpResponse("Invalid credentials! <br> <a href='/signup/'>Signup here</a>")
    return render(request, 'login.html')

def authors_and_sellers(request):
    users = CustomUser.objects.filter(public_visibility=True).order_by('username')
    return render(request, 'authors_and_sellers.html', {'users': users})

@login_required
def upload_file(request):
    files = UploadedFiles.objects.filter(user=request.user)
    if request.method == 'POST':
        form = UploadedFilesForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)
            uploaded_file.user = request.user
            uploaded_file.save()
            return redirect('upload_file')
    else:
        form = UploadedFilesForm()
    return render(request, 'uploadfiles.html', {'form': form, 'files': files})

def logout_view(request):
    logout(request)
    return redirect('login')

# Modified RegisterUser view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

@method_decorator(csrf_exempt, name='dispatch')
class RegisterUser(APIView):
    def post(self, request): # ← Starts when API receives POST request
        try:
            serializer = UserSerializer(data=request.data)# Validates data
            if serializer.is_valid():
                user = serializer.save()# Creates user using serializer
                token_obj, _ = Token.objects.get_or_create(user=user)# Creates auth token
                return Response({# ← Ends by returning token and user data
                    'status': 200,
                    'payload': serializer.data,
                    'token': str(token_obj),
                    'message': 'your data is saved'
                })
            return Response({
                'status': 400,
                'errors': serializer.errors,
                'message': 'Validation error'
            })
        except Exception as e:
            print(str(e))  # For debugging
            return Response({
                'status': 500,
                'errors': str(e),
                'message': 'server error'
            })
        

# Serializer for file
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFiles
        fields = [
            'id',
            'book_title',
            'book_description', 
            'visibility',
            'cost',
            'year_of_published',
            'file_upload'  # This must match your model field name exactly
        ]

# API view for accessing files
class UserFilesView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):# ← Starts when API receives GET request
        try:
            files = UploadedFiles.objects.filter(user=request.user)# Gets user's files
            serializer = FileSerializer(files, many=True)# Converts to JSON
            return Response({# ← Ends by returning file data
                'status': 'success',
                'data': serializer.data
            })
        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=500)