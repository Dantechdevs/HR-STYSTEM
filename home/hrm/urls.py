
from django.urls import path, include
from.import views

urlpatterns = [
    path('',views.home, name='home.html'),
    path('manage.html',views.manage,name='manage.html'),
    path('leadership-manage.html',views.leadership,name='leadership-manage.html'),
    path('super-admin.html',views.super_admin,name='super-admin.html'),
    path('employee.html',views.employee,name='employee.html'),
    path('add-employee.html',views.add_employee,name='add-employee.html'), 
    path('register.html',views.register,name='register.html'),
    path('login.html',views.login,name='login.html'),
    path('profile.html',views.profile,name='profile.html'),
    path('contact.html',views.contact,name='contact.html'),
    path('settings.html',views.settings,name='settings.html'),
    path('settings-timeoff.html',views.settings_timeoff,name='settings-timeoff.html'),
    path('index-employee.html',views.index_employee,name='index-employee.html'),
]
