# accounts/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile_home, name='profile_home'),
]
