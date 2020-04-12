from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('addnotice', views.addnotice, name='addnotice'),
    path('notices', views.notices, name='notices'),
    path('students', views.students, name='students'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('logout', views.logout, name='logout'),
]