
from django.urls import path, include
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('manage.html',views.manage,name='manage.html'),
    path('leadership-manage.html',views.leadership,name='leadership-manage.html'),
    path('super-admin.html',views.super_admin,name='super-admin.html'),
    
]
