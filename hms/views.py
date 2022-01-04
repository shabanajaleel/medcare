from django.shortcuts import render
from hmsadmin.models import *
from . models import *

def Home(request):
    obj1=departmentAdd.objects.all()
    for i in obj1:
        print(i.depname)
    return render(request,'index.html',{'dep':obj1})


    

def Homehead(request):    
    return render(request,'home.html',)

def fndepart(request,depid):
    obj1=departmentAdd.objects.all()
    obj2=departmentAdd.objects.filter(id=depid)
    obj3=doctoradd.objects.filter(department_id=depid,status=1)
    
    return render(request,'depview.html',{'dep1':obj2,'dep':obj1,'doc':obj3})

def fnqueries(request):
    try:
        if request.method=="POST":
            name=request.POST['name']
            print(name)
            email=request.POST['email']
            subject=request.POST['subject']
            message=request.POST['message']
            obj1=patientqueries(name=name,email=email,subject=subject,messsage=message)
            obj1.save()
            return render(request,'index.html',{'msg':"your query submitted succesfully.You will be contacted soon "})

    except Exception as e:print(e)

    


    
