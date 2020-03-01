from django.shortcuts import render
from .models import *
# Create your views here.
def showindex(request):
    return render(request,'index.html')
def checklogin(request):
    username=request.POST['t1']
    password=request.POST['t2']
    print(username,password)
    try:
        t_obj=Trainer.objects.get(username=username,password=password)
        if t_obj:
            print('t_obj')
            request.session['t_obj']=t_obj.id
            return render(request,"trainer_home.html",{'t_obj':t_obj})
    except:
        try:
            stu_obj=Student.objects.get(username=username,password=password)
            if stu_obj:
                print('stu_obj')
                request.session['stu_obj'] = stu_obj.id
                return render(request,'student_home.html',{'stu_obj':stu_obj})
        except:
            return render(request,'index.html',{'msg':'invalid Credentials'})

def allstudents(request):
    t_id=request.GET['id']
    t_obj=Trainer.objects.get(id=t_id)
    s_obj=Student.objects.all()
    return render(request,'student_details.html',{'s_obj':s_obj,'t_obj':t_obj})
def student_res_details(s_obj,stu_res_obj):
    dict = {}
    if not stu_res_obj:
        for x in s_obj:
            dict[x.id] = {'stu_id': x.id, 'stu_name': x.username}
    else:
        for x in s_obj:
            for y in stu_res_obj:
                if x.id == y.student.id:
                    dict[x.id]={'stu_id':x.id,'stu_name':x.username,'res1':y.res1,'res2':y.res2,'res3':y.avg,'available':'yes'}
                else:
                    try:
                        if dict[x.id]:
                            pass
                        else:
                            dict[x.id] = {'stu_id': x.id, 'stu_name': x.username}
                    except:
                        dict[x.id] = {'stu_id': x.id, 'stu_name': x.username}
    return dict
def studentres(request):
    t_id=request.GET['id']
    t_obj=Trainer.objects.get(id=t_id)
    s_obj=Student.objects.all()
    stu_res_obj = StudentResult.objects.filter(trainer=t_obj)
    dict=student_res_details(s_obj,stu_res_obj)
    return render(request,'student_results.html',{'s_obj':s_obj,'t_obj':t_obj,'res':dict})
def savestudentres(request):
    t_id=request.POST['tid']
    s_id=request.POST['sid']
    res1=request.POST['res1']
    res2=request.POST['res2']
    avg=request.POST['res3']
    t_obj=Trainer.objects.get(id=t_id)
    stu_obj=Student.objects.get(id=s_id)
    s_obj=Student.objects.all()
    StudentResult(trainer=t_obj,student=stu_obj,res1=res1,res2=res2,avg=avg).save()
    stu_res_obj=StudentResult.objects.filter(trainer=t_obj)
    dict=student_res_details(s_obj,stu_res_obj)

    return render(request,'student_results.html',{'s_obj':s_obj,'t_obj':t_obj,'res':dict})
def updatestudentres(request):
    t_id=request.POST['tid']
    s_id=request.POST['sid']
    res1=request.POST['res1']
    res2=request.POST['res2']
    avg=request.POST['res3']
    t_obj=Trainer.objects.get(id=t_id)
    stu_obj=Student.objects.get(id=s_id)
    s_obj=Student.objects.all()
    StudentResult.objects.filter(student=stu_obj,trainer=t_obj).update(res1=res1,res2=res2,avg=avg)
    stu_res_obj=StudentResult.objects.filter(trainer=t_obj)
    dict=student_res_details(s_obj,stu_res_obj)

    return render(request,'student_results.html',{'s_obj':s_obj,'t_obj':t_obj,'res':dict})
def finalreport(request):
    trainer=Trainer.objects.all()

    dict={}
    for x in trainer:

        tstures=StudentResult.objects.filter(trainer=x)
        if tstures:
            for y in tstures:

                try:
                    if dict[y.student.username]:
                        dict[y.student.username].update({y.trainer.username:y.avg})
                    else:
                        dict[y.student.username]= {y.trainer.username:y.avg}
                except:

                    dict[y.student.username] = {y.trainer.username: y.avg}
        else:
            for y in Student.objects.all():
                if dict[y.username] :
                    dict[y.username].update({x.username: 'NA'})
                else:
                    dict[y.username].update({x.username: 'NA'})
    return  render(request,'finalreport.html',{'res':dict,'trainers':Trainer.objects.all()})

