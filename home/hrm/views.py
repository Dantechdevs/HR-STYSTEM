from django.shortcuts import render, redirect



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
    
    return render(request, 'employee.html', {})

def add_employee(request):
    
    return render(request, 'add-employee.html', {})
def index_employee (request):
    
    return render(request, 'index-employee.html', {})


def profile(request):
    
    return render(request, 'profile.html', {})

def register(request):
    
    return render(request, 'register.html', {})
def login(request):
    
    return render(request, 'login.html', {})


def contact(request):
    return render(request, 'contact.html', {})

def settings(request):
    return render(request, 'settings.html', {}) 

def settings_timeoff(request):  
    return render(request,'settings-timeoff.html', {}) 

def profile_document(request):
    return render(request, 'profile-document.html', {})
