from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File
from django.contrib.auth.models import User, auth

from django.http import HttpResponse
from .models import Notice
from .models import Student
from .models import UImage

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from . import pt

def index(request):
    # user = User.objects.create_user(username='admin', password='admin')
    # user.save()
    if request.method=='POST':
        uname = request.POST['uname']
        pwd = request.POST['passwd']

        user = auth.authenticate(username=uname, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'index.html', {'msg': 'err'})
    else:
        return render(request, 'index.html')


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('/')


def addnotice(request):
    if request.user.is_authenticated:
        return render(request, 'addnotice.html')
    else:
        return redirect('/')

def addnprocess(request):
    if request.user.is_authenticated:
        dprt = request.POST['dpt']
        aca = request.POST['acayear']
        exp = request.POST['expdate']
        tpc = request.POST['topic']
        cont = request.POST['tcontent']

        Notice.objects.create(dpt = dprt, acayear = aca, expdate = exp, topic = tpc, content = cont)

        return HttpResponse('')
    else:
        return redirect('/')
    

def addsprocess(request):
    if request.user.is_authenticated:
        fnam = request.POST['fname']
        lnam = request.POST['lname']
        uindex = request.POST['uindex']
        reg = request.POST['regno']
        dprt = request.POST['dpt']
        acayr = request.POST['acayear']

        varr = pt.test()

        Student.objects.create(id = uindex, regno = reg, fname = fnam, lname = lnam, dpt = dprt, acayear = acayr, funq = varr)

        return HttpResponse(varr)
    else:
        return redirect('/')
    

@csrf_exempt
def serverscript(request):
    if request.user.is_authenticated:
        file = request.FILES['webcam']
        req = request.GET['Req']
        frmname = request.GET['Fnam']

        nam = frmname + '.jpg'

        default_storage.save( nam, ContentFile(file.read()))
        
        UImage.objects.create(imgname = str(nam), uindex = str(req))

        return HttpResponse(nam)
    else:
        return redirect('/')


def notices(request):
    if request.user.is_authenticated:
        obj = Notice.objects.all().order_by('-id')

        return render(request, 'notices.html', {'notices': obj})
    else:
        return redirect('/')
    


def students(request):

    if request.user.is_authenticated:
        obj = Student.objects.all().order_by('-id')
        return render(request, 'students.html', {'students': obj})
    else:
        return redirect('/')
    


def addstudent(request):
    if request.user.is_authenticated:
        return render(request, 'addstudent.html')
    else:
        return redirect('/')
    


def nedit(request):
    if request.user.is_authenticated:
        n = Notice()
        n.id = request.GET['Nid']
        n.topic = request.GET['Topic']
        n.content = request.GET['Content']
        n.dpt = request.GET['Dpt']
        n.acayear = request.GET['Aca']
        n.expdate = request.GET['Exp']

        return render(request, 'nedit.html', {'notice': n})
    else:
        return redirect('/')
    


def editnprocess(request):
    if request.user.is_authenticated:
        nnum = request.POST['nid_n']
        topic = request.POST['topic']
        content = request.POST['tcontent']
        dprt = request.POST['dprt']
        acayear = request.POST['acayear']
        expdate = request.POST['expdate']

        e_notice = Notice.objects.get(id=nnum)

        e_notice.dpt = dprt
        e_notice.acayear = acayear
        e_notice.expdate = expdate
        e_notice.topic = topic
        e_notice.content = content

        e_notice.save()

        return HttpResponse('')
    else:
        return redirect('/')
    


def delnprocess(request):

    if request.user.is_authenticated:
        nnum = request.POST['nindex']

        d_notice = Notice.objects.get(id=nnum)

        d_notice.delete()

        return HttpResponse('')
    else:
        return redirect('/')

    


def sedit(request):
    if request.user.is_authenticated:
        s = Student()
        s.id = request.GET['Sid']
        s.fname = request.GET['Fnam']
        s.lname = request.GET['Lnam']
        s.regno = request.GET['Reg']
        s.dpt = request.GET['Dpt']
        s.acayear = request.GET['Aca']

        return render(request, 'sedit.html', {'student': s})
    else:
        return redirect('/')
    

def editsprocess(request):
    if request.user.is_authenticated:
        snum = request.POST['uin']
        fir = request.POST['fnam']
        las = request.POST['lnam']
        regnn = request.POST['regn']
        dpmt = request.POST['dprt']
        acyr = request.POST['acayr']

        e_stu = Student.objects.get(id=snum)

        e_stu.regno = regnn
        e_stu.fname = fir
        e_stu.lname = las
        e_stu.dpt = dpmt
        e_stu.acayear = acyr

        e_stu.save()

        return HttpResponse('')
    else:
        return redirect('/')

    


def delsprocess(request):

    if request.user.is_authenticated:
        snum = request.POST['sindex']

        d_stu = Student.objects.get(id=snum)

        d_stu.delete()

        return HttpResponse('')
    else:
        return redirect('/')

    


def logout(request):
    auth.logout(request)

    return redirect('/')