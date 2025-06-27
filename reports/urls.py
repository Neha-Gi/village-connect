# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_home, name='report_home'),
]
