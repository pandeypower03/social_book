from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    
    path("signup/",views.signup_view,name="signup"),
    path('login/', views.login_view, name='login'),
]
