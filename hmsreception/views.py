from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from .models import appointments
from hmsadmin.models import departmentAdd, doctoradd,dropschedule
from django.contrib import messages

# Create your views here.
#load dashbord
def fnrecdash(request):
    return render(request,"recdashbord.html")

#select dep to the select box of appointment form..

def fnappointment(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        age=request.POST['age']
        mobile=request.POST['mobile']
        address=request.POST['address']
        department=request.POST['department']
        doc=request.POST['doc']
        day=request.POST['day']
        obj=appointments(fname=fname,lname=lname,age=age,mobile=mobile,address=address,dep_id=department,doc_id=doc,day_id=day,status=0).save()
        
        messages.success(request,'Taken Appointment Successfully')
        return redirect(fnappointment)
        

    else:
        depselect=departmentAdd.objects.all()
        return render(request,'addappointment.html',{'dep':depselect})

# doctor appointment view

def fnviewappointment(request):
    doctors=doctoradd.objects.filter(status=1)
    return render(request,'viewappointment.html',{'doc':doctors})

#select dr to the select box of appointment form..

def fnselectdr(request):
    if request.method=='POST':
        depname=request.POST['dep']
        dep=departmentAdd.objects.get(id=depname)
        doctor=doctoradd.objects.filter(department_id=dep)
        load_doctor=[{'id':i.id,'fname':i.fname} for i in doctor]
        return JsonResponse({'data':load_doctor})

def fnselectday(request):
    if request.method=='POST':
        doc=request.POST['doc']
        doctor=doctoradd.objects.get(id=doc)
        selectday=dropschedule.objects.filter(doctorid_id=doctor)
        load_day=[{'id':i.id,'day':i.day} for i in selectday]
        
        return JsonResponse({'data':load_day})

def fnviewdoctor(request):
    if request.method=='POST':
        postname=request.POST['depdoc']
        department=departmentAdd.objects.filter(depname=postname).exists()
        if department==True:
            dep=departmentAdd.objects.get(depname=postname)
            depid=dep.id
            selectdr=doctoradd.objects.filter(department_id=depid)
            return render(request,'doctordetails.html',{'doc':selectdr})
        else:
            doctor=doctoradd.objects.filter(fname=postname).exists()
            if doctor==True:
                doctortable=doctoradd.objects.filter(fname=postname)
                return render(request,'doctordetails.html',{'doc':doctortable})
            else:
                return render(request,'viewdoctor.html',{'msg':"invalid department or doctor"})


    return render(request,'viewdoctor.html')

