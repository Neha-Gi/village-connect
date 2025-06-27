# delivery/views.py
from django.http import HttpResponse

def delivery_home(request):
    return HttpResponse("Welcome to the Delivery section!")
