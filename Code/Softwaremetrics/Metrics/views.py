import os
import ast
from datetime import *
import re
from msilib.schema import File
from random import randint
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
#from h5py._errors import filename_encode

from Metrics.forms import userForm, UploadfileForm
from Metrics.models import user, upload


def index(request):
    return render(request,'index.html')

def adminpage(request):
    return render(request,'admin/adminpage.html')

def userpage(request):
    return render(request,"user/userpage.html")

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upass']
        if uname == 'admin' and passwd=='admin':
            return render(request,"admin/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")


def logout(request):
    return render(request,'index.html')


def userlogin(request):
    return render(request,"user/userlogin.html")

def userregister(request):
    if request.method=='POST':
        form1=userForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "user/userlogin.html")
            #return HttpResponse("registreration succesfully completed")
        else:
            print("form not valied")
            return HttpResponse("form not valied")
    else:
        form=userForm()
        return render(request,"user/userregister.html",{"form":form})

def viewuserdata(request):
    s=user.objects.all()
    return render(request,"admin/viewuserdata.html",{"qs":s})

def activateuser(request):
    if request.method =='GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        user.objects.filter(id=uname).update(status=status)
        qs=user.objects.all()
        return render(request,"admin/viewuserdata.html",{"qs":qs})


def userlogincheck(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        print(uname)
        upasswd = request.POST.get('upasswd')
        print(upasswd)
        try:
            check = user.objects.get(name=uname, passwd=upasswd)
            # print('usid',usid,'pswd',pswd)
            print(check)
            # request.session['name'] = check.name
            # print("name",check.name)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['mail'] = check.mail
                return render(request, 'user/userpage.html')
            else:
                messages.success(request, 'user is not activated')
                return render(request, 'user/userlogin.html')
        except Exception as e:
            print('Exception is ',str(e))
            pass
        messages.success(request,'Invalid Email id and password')
        return render(request,'user/userlogin.html')

"""def activateuser(request):
    if request.method=='GET':
        uname = request.GET.get('uname')
        authkey = random_with_N_digits(8)
        status = 'activated'
        print("uname = ",uname,authkey,status)
        user.objects.filter(name=uname).update( status=status)
        userdata = user.objects.all()
        return render(request,'admin/viewuserdata.html',{'object':userdata})"""

def userlogincheck1(request):
    if request.method == "POST":
        email = request.POST.get('uname')
        pswd = request.POST.get('upasswd')
        print("Email = ", email, ' Password = ', pswd)
        try:
            check = user.objects.get(name=email,passwd=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "Activated":
                request.session['id'] = check.id
                request.session['name'] = check.name
                request.session['email'] = check.mail
                print("User id At", check.id, status)
                return render(request, 'user/userpage.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'user/userlogin.html')
            # return render(request, 'user/userpage.html',{})
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Email id and password')
    return render(request, 'user/userlogin.html')



def uploadfile(request):
    if request.method == 'POST':
        form = UploadfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('user/upload_list.html')
    else:
        form = UploadfileForm()
    return render(request, 'user/uploadfile.html', {'form': form})

def upload_list(request):
    files = File.objects.all()
    return render(request, 'user/upload_list.html', {'files': files})


def viewfile(request):
    filedata = upload.objects.all()
    return render(request, 'admin/viewfiles.html', {'object': filedata})

def viewfildata(request):
    filedata = upload.objects.all()
    return render(request, 'user/viewfiledata.html', {'object': filedata})

def userfiledata(request):
    if request.method == "GET":
        file = request.GET.get('id')
        try:
            print("file", file)
            head, fileName = os.path.split(file)

            fPath = settings.MEDIA_ROOT + '\\' + 'files\pdfs' + '\\' + fileName

            f = open(fPath)
            loc = 0
            wordcount = 0
            chrcount = 0
            cmntcount = 0
            classcount = 0
            for line in f:
                loc = loc + 1
                chrcount = chrcount + len(line)
                word = line.split(' ')
                wordcount = wordcount + len(word)
                if line.startswith('#'):
                    cmntcount = cmntcount + 1
                if line.startswith('class'):
                    classcount = classcount + 1
            f = open(fPath)
            fd = f.read()
            stats = os.stat(fPath)
            s = datetime.fromtimestamp(stats.st_atime)
            s1 = datetime.fromtimestamp(stats.st_mtime)
            size1 = stats.st_size
            print("file size in bytes:", size1)
            print('class-count', classcount)
            with open(fPath) as f:
                tree = ast.parse(f.read())
                func = sum(isinstance(exp, ast.FunctionDef) for exp in tree.body)
            '''it's about finding condintion statements and loops'''
            f = open(fPath)
            lpcountif = lpcountelif = lpcountelse = lpcountfor = 0
            line = f.readlines()
            for x in line:
                if re.search('if ', x):
                    lpcountif = lpcountif + 1
                if re.search('elif ', x):
                    lpcountelif = lpcountelif + 1
                if re.search('else ', x):
                    lpcountelse = lpcountelse + 1
                if re.search('for ', x):
                    lpcountfor = lpcountfor + 1
            cmplx = lpcountif + lpcountelif + lpcountelse + lpcountfor
            if cmplx <= 10:
                perfrmance = "normal"
            elif cmplx > 10 and cmplx <= 20:
                perfrmance = "moderate"
            else:
                perfrmance = "high"


            message = {"filename": f.name, "lines": loc, "words": wordcount, "charecters": chrcount, "content": fd,
                       "functionscount": func, "commentlinescount": cmntcount, "lastmodifiedtime": s1,
                       "lastaccessedtime": s, "classescount": classcount, "ifloop": lpcountif, "elifloop": lpcountelif,
                       "elseloop": lpcountelse,"filesize":size1, "forloop": lpcountfor,"cmplx":cmplx,"perf":perfrmance}
            return render(request, "user/userfiledata.html", {"message": message})
        except Exception as e:
            print('Exception is ', str(e))
            messages.success(request, 'Invalid Details')
        return render(request, 'user/userfiledata.html')


def filedata(request):
    if request.method == "GET":
        file = request.GET.get('id')
        try:
            print("file", file)
            head, fileName = os.path.split(file)
            fPath = settings.MEDIA_ROOT + '\\' + 'files\pdfs' + '\\' + fileName
            f = open(fPath)
            loc = 0
            wordcount = 0
            chrcount = 0
            cmntcount = 0
            classcount = 0
            for line in f:
                loc = loc + 1
                chrcount = chrcount + len(line)
                word = line.split(' ')
                wordcount = wordcount + len(word)
                if line.startswith('#'):
                    cmntcount = cmntcount + 1
                if line.startswith('class'):
                    classcount = classcount + 1
            f = open(fPath)
            fd = f.read()
            stats = os.stat(fPath)
            s = datetime.fromtimestamp(stats.st_atime)
            s1 = datetime.fromtimestamp(stats.st_mtime)
            size1 = stats.st_size
            print("file size in bytes:", size1)
            print('class-count', classcount)
            with open(fPath) as f:
                tree = ast.parse(f.read())
                func = sum(isinstance(exp, ast.FunctionDef) for exp in tree.body)
            '''it's about finding condintion statements and loops'''
            f = open(fPath)
            lpcountif = lpcountelif = lpcountelse = lpcountfor =lpcountwhile=countwith=countexcept=countfinally=0
            line = f.readlines()
            for x in line:
                if re.search('if ', x):
                    lpcountif = lpcountif + 1
                if re.search('elif ', x):
                    lpcountelif = lpcountelif + 1
                if re.search('else ', x):
                    lpcountelse = lpcountelse + 1
                if re.search('for ', x):
                    lpcountfor = lpcountfor + 1
                if re.search('while ', x):
                    lpcountwhile = lpcountwhile + 1
                if re.search('with ', x):
                    countwith=countwith+1
                if re.search('except:', x):
                    countexcept=countexcept+1
                if re.search('finally:', x):
                    countfinally=countfinally+1


            cmplx=lpcountif+lpcountelif+lpcountelse+lpcountwhile+lpcountfor+1+countexcept+countfinally
            if cmplx<=5 and cmplx>=1:
                perfrmance="Low-simple block"
                rank="A"
            elif cmplx>=6 and cmplx<=10:
                perfrmance="low"
                rank="B"
            elif cmplx>=11 and cmplx<=20:
                perfrmance = "Moderate"
                rank = "C"
            elif cmplx>=21 and cmplx<=30:
                perfrmance = "More than Moderate"
                rank = "D"

            elif cmplx>=31 and cmplx<=40:
                perfrmance = "high"
                rank = "E"
            else:
                perfrmance="very high"
                rank='F'
            message = {"filename": f.name, "lines": loc, "words": wordcount, "charecters": chrcount, "content": fd,
                       "functionscount": func, "commentlinescount": cmntcount, "lastmodifiedtime": s1,
                       "lastaccessedtime": s, "classescount": classcount, "ifloop": lpcountif, "elifloop": lpcountelif,
                       "elseloop": lpcountelse,"filesize":size1,"countexcept":countexcept,"countfinally":countfinally, "forloop": lpcountfor,"whileloop":lpcountwhile,"cmplx":cmplx,"rank":rank,"perf":perfrmance}
            return render(request, "admin/filedata.html", {"message": message})
        except Exception as e:
            print('Exception is ', str(e))
            messages.success(request, 'Invalid Details')
        return render(request, 'admin/filedata.html')


