from django.shortcuts import render

# Create your views here.
# messaging/views.py
from django.http import HttpResponse

def messaging_home(request):
    return HttpResponse("Welcome to the Messaging!")
