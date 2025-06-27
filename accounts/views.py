from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
# accounts/views.py
from django.http import HttpResponse

def profile_home(request):
    return HttpResponse("Welcome to the profile page.")
