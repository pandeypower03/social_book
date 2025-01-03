from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def signup_view(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return HttpResponse("Signup successful!")
    return render(request,'home.html')