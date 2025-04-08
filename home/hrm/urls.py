
from django.urls import path, include
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('manage.html',views.manage,name='manage.html'),
]
