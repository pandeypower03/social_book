from django.urls import path
from . import views
from django.contrib import admin
from .views import authors_and_sellers
from .views import logout_view



urlpatterns = [
    
    path("signup/",views.signup_view,name="signup"),
    path('login/', views.login_view, name='login'),
    path('authors-and-sellers/', authors_and_sellers, name='authors_and_sellers'),
   
    path('upload/', views.upload_file, name='upload_file'),
    path('logout/', logout_view, name='logout'),
   
]

