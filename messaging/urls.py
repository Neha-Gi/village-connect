# messaging/urls.py
from django.urls import path
from . import views


urlpatterns = [
    path('', views.messaging_home, name='profile_messaging'),
]
