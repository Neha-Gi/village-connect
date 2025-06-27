"""
URL configuration for village_connect project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

def home_view(request):
    return render(request, 'home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
]


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),
    
    # Home page
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
    # Authentication (django-allauth)
    path('accounts/', include('allauth.urls')),
    
    # Custom accounts app
    path('profile/', include('accounts.urls')),
    
    # Marketplace
    path('marketplace/', include('marketplace.urls')),
    
    # Wallet
    path('wallet/', include('wallet.urls')),
    
    # Messaging
    path('messages/', include('messaging.urls')),
    
    # Delivery
    path('delivery/', include('delivery.urls')),
    
    # Reports
    path('reports/', include('reports.urls')),
    
    # API
   # path('api/v1/', include('village_connect.api_urls')),
    
    # QR Code
    path('qr_code/', include('qr_code.urls', namespace="qr_code")),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Custom admin site headers
admin.site.site_header = "Village Connect Administration"
admin.site.site_title = "Village Connect Admin"
admin.site.index_title = "Welcome to Village Connect Administration"
from django.contrib import admin
from django.urls import path
from django.shortcuts import render

