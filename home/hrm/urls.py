
from django.urls import path, include
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('manage.html',views.manage,name='manage.html'),
    path('leadership-manage.html',views.leadership,name='leadership-manage.html'),
    path('super-admin.html',views.super_admin,name='super-admin.html'),
    path('employee.html',views.employee,name='employee.html'),
    path('add-employee.html',views.add_employee,name='add-employee.html'), 
    path('register.html',views.register,name='register.html'),
    path('login.html',views.login,name='login.html'),
    path('profile.html',views.profile,name='profile.html')
]
