from django.shortcuts import render
from hmsadmin.models import doctoradd

def fndashbord(request):
    if request.session.has_key('doctor'):
        session=request.session['doctor']
        print(session)
        obj=doctoradd.objects.get(id=session)
        print(obj.fname)
    
    return render(request,"docdashbord.html",{'doc':obj})

def fnheader(request):
    return render(request,"docheader.html")

def fnprofile(request):
    session=request.session['doctor']
    print(session)
    obj8=doctoradd.objects.filter(id=session)
    return render(request,'profile.html',{'pro':obj8})



