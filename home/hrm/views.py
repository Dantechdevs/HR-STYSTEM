from django.shortcuts import render

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
    
    return render(request, 'add_employee.html', {})