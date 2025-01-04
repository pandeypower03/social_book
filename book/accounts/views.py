from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import CustomUser
from django.shortcuts import  redirect
from .forms import UploadedFilesForm
from .models import UploadedFiles



from django.contrib.auth import get_user_model
User= get_user_model()
# Create your views here.
def signup_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return HttpResponse("Signup successful!")
    return render(request,'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse("Login successful!")
        else:
            return HttpResponse("Invalid credentials! <br> <a href='/signup/'>Signup here</a>")

    return render(request, 'login.html')

#logic for rendering authors and sellerspage for user who has opted for public visibility

def authors_and_sellers(request):
    # Fetch users with public visibility
    users = CustomUser.objects.filter(public_visibility=True)

    #  Additional filters  sort by username
    users = users.order_by('username')  

    return render(request, 'authors_and_sellers.html', {'users': users})

def upload_file(request):
    files = UploadedFiles.objects.all()  # Fetch existing files for display

    if request.method == 'POST':
        form = UploadedFilesForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()  # Save the form data to the database
            # Re-fetch files to include the newly added file
            files = UploadedFiles.objects.all()

    else:
        form = UploadedFilesForm()  # Display an empty form for GET requests

    return render(request, 'uploadfiles.html', {'form': form, 'files': files})
