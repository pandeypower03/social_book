from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import CustomUser, UploadedFiles
from .forms import UploadedFilesForm
from django.urls import reverse
from django.contrib.auth import logout

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Ensure the user is created correctly
        try:
            user = CustomUser.objects.create_user(username=username, password=password)
            return redirect('login')  # Redirect to login after successful signup
        except Exception as e:
            return HttpResponse(f"Error: {e}")  # Show error if there are any issues while creating the user

    return render(request, 'home.html')  # Render the signup page

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', reverse('upload_file'))  # Redirect to upload file
            return redirect(next_url)
        else:
            return HttpResponse("Invalid credentials! <br> <a href='/signup/'>Signup here</a>")

    return render(request, 'login.html')

def authors_and_sellers(request):
    # Fetch users with public visibility
    users = CustomUser.objects.filter(public_visibility=True)
    # Additional filters sort by username
    users = users.order_by('username')  

    return render(request, 'authors_and_sellers.html', {'users': users})

@login_required
def upload_file(request):
    # Filter files by the current logged-in user
    files = UploadedFiles.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = UploadedFilesForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)  # Don't save the file yet
            uploaded_file.user = request.user  # Assign the current user to the file
            uploaded_file.save()  # Now save the file with the user assigned
            return redirect('upload_file')
    else:
        form = UploadedFilesForm()

    return render(request, 'uploadfiles.html', {'form': form, 'files': files})

def logout_view(request):
    logout(request)
    return redirect('login')
