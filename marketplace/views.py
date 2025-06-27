from django.shortcuts import render

# Create your views here.
# marketplace/views.py
from django.http import HttpResponse

def marketplace_home(request):
    return HttpResponse("Welcome to the Marketplace!")
