from django.urls import path

from . import views



from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('addnotice', views.addnotice, name='addnotice'),
    path('notices', views.notices, name='notices'),
    path('students', views.students, name='students'),
    path('addstudent', views.addstudent, name='addstudent'),
    path('logout', views.logout, name='logout'),
    path('addnprocess', views.addnprocess, name='addnprocess'),
    path('addsprocess', views.addsprocess, name='addsprocess'),
    path('serverscript', views.serverscript, name='serverscript'),
    path('nedit', views.nedit, name='nedit'),
    path('editnprocess', views.editnprocess, name='editnprocess'),
    path('delnprocess', views.delnprocess, name='delnprocess'),
    path('sedit', views.sedit, name='sedit'),
    path('editsprocess', views.editsprocess, name='editsprocess'),
    path('delsprocess', views.delsprocess, name='delsprocess'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
