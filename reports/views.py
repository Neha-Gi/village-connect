from django.shortcuts import render

# Create your views here.
# wallet/views.py
from django.http import HttpResponse

def report_home(request):
    return HttpResponse("Welcome to the Report!")
