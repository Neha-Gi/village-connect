# wallet/views.py
from django.http import HttpResponse

def wallet_home(request):
    return HttpResponse("Welcome to the Wallet!")
