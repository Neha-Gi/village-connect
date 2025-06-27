import os
import subprocess
import sys

def create_django_project():
    print("Village Connect - Django Project Setup")
    print("=====================================\n")
    
    print("This script shows you how to create the Django project structure.\n")
    
    print("Step 1: Create and activate virtual environment")
    print("-----------------------------------------------")
    print("python -m venv village_connect_env")
    print("# On Windows:")
    print("village_connect_env\\Scripts\\activate")
    print("# On macOS/Linux:")
    print("source village_connect_env/bin/activate")
    print()
    
    print("Step 2: Install Django and required packages")
    print("--------------------------------------------")
    packages = [
        "Django>=4.2.0",
        "django-crispy-forms",
        "crispy-bootstrap5",
        "Pillow",
        "django-allauth",
        "djangorestframework",
        "django-qr-code",
        "django-channels",
        "django-modeltranslation",
        "django-phonenumber-field[phonenumberslite]",
        "django-storages",
        "django-cors-headers",
        "psycopg2-binary",
        "redis",
        "celery",
        "python-decouple",
        "qrcode[pil]",
        "googletrans==4.0.0rc1",
    ]
    
    print("pip install " + " ".join(packages))
    print()
    
    print("Step 3: Create Django project")
    print("-----------------------------")
    print("django-admin startproject village_connect")
    print("cd village_connect")
    print()
    
    print("Step 4: Create Django apps")
    print("-------------------------")
    apps = [
        "accounts",
        "marketplace", 
        "wallet",
        "messaging",
        "delivery",
        "reports"
    ]
    
    for app in apps:
        print(f"python manage.py startapp {app}")
    print()
    
    print("After running these commands, you'll have the complete project structure!")
    print("The manage.py file will be in the root directory of your project.")

create_django_project()
