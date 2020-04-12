from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'home.html')


def addnotice(request):
    return render(request, 'addnotice.html')


def notices(request):
    return render(request, 'notices.html')


def students(request):
    return render(request, 'students.html')


def addstudent(request):
    return render(request, 'addstudent.html')


def logout(request):
    return render(request, 'logout.html')