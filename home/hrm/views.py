from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from .models import Employee
from django.contrib import messages
from django.core.exceptions import ValidationError


# Create your views here.
def home(request):
    return render(request, 'home.html', {})

    
def manage(request):
    
    return render(request, 'manage.html', {})

    
def leadership(request):
    
    return render(request, 'leadership-manage.html', {})    

def super_admin(request):
    
    return render(request, 'super-admin.html', {})

# employee
def employee(request):
    
    return render(request, 'employee.html', context)

def add_employee(request):
    
    return render(request, 'add-employee.html', {})
