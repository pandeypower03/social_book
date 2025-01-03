from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

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