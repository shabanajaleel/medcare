from django.shortcuts import render,redirect
from hms.models import *
from . models import *
from random import random
from django.core.files.storage import FileSystemStorage

def fnLogin(request):
    
    try:
        if request.method=='POST':
            role=request.POST['module']
            if role=='admin':
                uname=request.POST['username']
                password=request.POST['password']
                obj=AdminRegister.objects.get(username=uname,password=password)      
                request.session['admin']=obj.id
                request.session['admin']
                return render(request,'dashbord.html',{'user':obj})
            if role=='doctor':
                username=request.POST['username']
                print(username)
                password=request.POST['password']
                print(password)
                obj2=doctoradd.objects.get(email=username,password=password)
                request.session['doctor']=obj2.id
                return redirect('/doctor/dashbord')

        else:return render(request,'login.html',{'msg':'invalid username or password'})
    except Exception as e:print(e)
    return render(request,'login.html')





def Header(request):
    return render(request,'Header.html')
    


def Doctor(request):
    if request.session.has_key('admin'):
        session=request.session['admin']
        obj=AdminRegister.objects.get(id=session)
        obj2=doctoradd.objects.filter(status=1)
        return render(request,'doctor.html',{"user":obj,"doc":obj2})
    else:return render(request,'login.html')

def fnadddoctor(request):
    obj1=departmentAdd.objects.all()
    return render(request,'adddoctor.html',{'dep':obj1})


def adddoctorfn(request):
    try:
        if request.method=="POST":
            docid=request.POST['docid']
            fname=request.POST['fname']
            lname=request.POST['lname']
            place=request.POST['place']
            age=request.POST['age']
            mobile=request.POST['mobile']
            email=request.POST['email']
            password=request.POST['password']
            quali=request.POST.getlist('quali')
            print(quali)
            dep=request.POST['dep']
            print(dep)
            inpimage=request.FILES['inputimage1']
            imagefile1=str(random())+inpimage.name
            newobj=FileSystemStorage()
            newobj.save(imagefile1,inpimage)
            print(inpimage)
            joindate=request.POST['date']
            print(joindate)
            exp=request.POST['exp']
            print(exp)
            address=request.POST['address']
            print(address)
            description=request.POST['description']
            print(description)
            obj2=doctoradd(docid=docid,fname=fname,lname=lname,place=place,age=age,email=email,mobile=mobile,password=password,quali=quali,department_id=dep,imagefile=imagefile1,joindate=joindate,experience=exp,address=address,description=description,status=1)
            obj2.save()
            return render(request,'adddoctor.html',{'msg':'inserted successfully'})
        else:
            request.session.has_key('admin')
            session=request.session['admin']
            obj=AdminRegister.objects.get(id=session)
            return render(request,'adddoctor.html',{"user":obj})
    except Exception as e:print(e)
    return render(request,'adddoctor.html',{'msg':'error'})
    

def fndeletedoc(request,docid):
    obj2=doctoradd.objects.filter(id=docid)
    obj2.update(status=0)
    return redirect('/admin/doctor/')




def Department(request):
    mysession=request.session['admin']
    if mysession:
        obj1=departmentAdd.objects.all()
    
        return render(request,'department.html',{'dep':obj1})
    else:
        return render(request,'login.html')

  
    

def Adddepartment(request):
    if request.method=='POST':
        depname=request.POST['dep']
        obj4=departmentAdd.objects.filter(depname=depname).exists()
        if obj4==False:
            depimage=request.FILES['inputimage']
            description=request.POST['description']
            imagefile=str(random())+depimage.name
            obj1=FileSystemStorage()
            obj1.save(imagefile,depimage)
            obj2=departmentAdd(depname=depname,imagefile=imagefile,description=description).save()
            return redirect('/admin/department/')
        else:
            return render(request,'adddepartment.html',{'msg':"department already exists"})
    else:return render(request,'adddepartment.html')

def updatedepartment(request,upd_id):

    obj4=departmentAdd.objects.filter(id=upd_id)
    print(upd_id)
    if obj4.exists():
        return render(request,'adddepartment.html',{'adddep':obj4})
    else:return render(request,'adddepartment.html')
            
    
def updatedep(request):
    try:
        if request.method=='POST':
            depname=request.POST['dep']
            print(depname)
            upd_id=request.POST['depid']
            print(upd_id)
            obj4=departmentAdd.objects.filter(depname=depname).exists()
            if obj4==False:
                depimage=request.FILES['inputimage1']
                imagefile=str(random())+depimage.name
                obj1=FileSystemStorage()
                obj1.save(imagefile,depimage)
                print(imagefile)
                if 'inputimage1' not in request.FILES:
                    print("hai")
                    obj4=departmentAdd.objects.filter(id=upd_id)
                    depimage1=obj4.imagefile
                    description=request.POST['description']
                    obj3=departmentAdd.objects.filter(id=upd_id).update(depname=depname,imagefile=depimage1,description=description)
                    return redirect('/admin/department/')
                else:
                    description=request.POST['description']
                    obj3=departmentAdd.objects.filter(id=upd_id).update(depname=depname,imagefile=imagefile,description=description)
                    return redirect('/admin/department/')
            else:
                obj4=departmentAdd.objects.get(id=upd_id)
                print("hai")
                departmentname=obj4.depname
                print(departmentname)
                if depname==departmentname:
                    description=request.POST['description']
                    depimage=request.FILES['inputimage1']
                    imagefile=str(random())+depimage.name
                    obj1=FileSystemStorage()
                    obj1.save(imagefile,depimage)
                    departmentAdd.objects.filter(id=upd_id).update(depname=depname,imagefile=imagefile,description=description)
                    return redirect('/admin/department/')
                else:return render(request,'adddepartment.html',{"msg":"department already exist"})

    except Exception as e:print(e)
    



    #     elif upd_id!=0 and obj4==False:
    #         depimage=request.FILES['inputimage1']
    #         if not depimage:
    #             obj4=departmentAdd.objects.filter(id=upd_id)
    #             depimage1=obj4.imagefile
    #             description=request.POST['description']
    #             obj3=departmentAdd.objects.filter(id=upd_id).update(depname=depname,imagefile=depimage1,description=description)
    #             return redirect('/admin/department/')
    #         else:
    #             description=request.POST['description']
    #             imagefile=str(random())+depimage.name
    #             obj1=FileSystemStorage()
    #             obj1.save(imagefile,depimage)
    #             obj3=departmentAdd.objects.filter(id=upd_id).update(depname=depname,imagefile=imagefile,description=description)
    #             return redirect('/admin/department/')
    #     elif upd_id!=0 and obj4==True:
    #         obj4=departmentAdd.objects.filter(id=upd_id)
    #         depname1=obj4.depname
    #         if depname==depname1:
    #             depimage=request.FILES['inputimage1']
    #             if not depimage:
    #                 obj4=departmentAdd.objects.filter(id=upd_id)
    #                 depimage1=obj4.imagefile
    #                 description=request.POST['description']
    #                 obj3=departmentAdd.objects.filter(id=upd_id).update(depname=depname,imagefile=depimage1,description=description)
    #                 return redirect('/admin/department/')
    #             else:
    #                 description=request.POST['description']
    #                 imagefile=str(random())+depimage.name
    #                 obj1=FileSystemStorage()
    #                 obj1.save(imagefile,depimage)
    #                 obj3=departmentAdd.objects.filter(id=upd_id).update(depname=depname,imagefile=imagefile,description=description)
    #                 return redirect('/admin/department/')
    #         else:return render(request,'adddepartment.html',{'msg':"department already exists"})
    # else:
    #     obj4=departmentAdd.objects.filter(id=upd_id)
    #     print(upd_id)
    #     if obj4.exists():

    #         return render(request,'adddepartment.html',{'adddep':obj4})
    #     else:return render(request,'adddepartment.html')
            
                

    



    
    # if request.method=='POST':
          
    #     depname=request.POST['dep']
    #     print(depname)
    #     depimage=request.FILES['inputimage']
    #     print(depimage)
    #     description=request.POST['description']
    #     print(description)
    #     imagefile=str(random())+depimage.name
    #     obj1=FileSystemStorage()
    #     obj1.save(imagefile,depimage)
    #     obj4=departmentAdd.objects.filter(depname=depname).exists()
          
    #     if upd_id==0:
    #         obj2=departmentAdd(depname=depname,imagefile=imagefile,description=description).save()
    #         return redirect('/admin/department/')
    #     else:
    #         print('hai')
    #         obj3=departmentAdd.objects.filter(id=upd_id).update(depname=depname,imagefile=imagefile,description=description)
    #         return redirect('/admin/department/')
    
    # else:
    #     obj4=departmentAdd.objects.filter(id=upd_id)
    #     print(upd_id)
    #     if obj4.exists():
    #         return render(request,'adddepartment.html',{'adddep':obj4})
    #     else:return render(request,'adddepartment.html')
        
    
      
    
    
    
  
    

def fnupdatedep(request,upd_id):
    
        obj2=departmentAdd.objects.filter(id=upd_id)
        return render(request,'adddepartment.html',{'user':obj2})
    


def fndelete(request,dep_id):
    obj2=departmentAdd.objects.get(id=dep_id)
    obj2.delete()
    return redirect('department/')
   

def fndeletequery(request,query_id):
    obj=patientqueries.objects.get(id=query_id)
    obj.delete()
    obj1=patientqueries.objects.all()
    return render(request,'queries.html',{'query':obj1})

def fnstaffcat(request):
    obj=staffcatogory.objects.all()
    return render(request,'staffcat.html',{"cat":obj})

def fnaddstaffcat(request):
    try:
        if request.method=='POST':
            id=request.POST['id']
            cat=request.POST['catogory']
            print(cat)
            if id:
                obj=staffcatogory.objects.filter(id=id)
                obj.update(catogoryname=cat)

            else:
                obj1=staffcatogory(catogoryname=cat)
                obj1.save()
                return render(request,'addstaffcat.html',{'msg':'added successfully'})

    except Exception as e:print(e)
    return render(request,'addstaffcat.html')


def fndeletecat(request,cat_id):
    obj=staffcatogory.objects.get(id=cat_id)
    obj.delete()
    obj1=staffcatogory.objects.all()
    return render(request,'staffcat.html',{'cat':obj1})


   

def fnstaff(request):
    obj=staffadd.objects.filter(status=1)
    return render(request,'staff.html',{'staff':obj})



def fnaddstaff(request):
    obj1=staffcatogory.objects.all()
    obj2=departmentAdd.objects.all()
    return render(request,'addstaff.html',{'cat':obj1,'dep':obj2})

def fnstaffadd(request):
    try:
        if request.method=='POST':
            staffid=request.POST['staffid']
            print(staffid)
            fname=request.POST['fname']
            print(fname)
            lname=request.POST['lname']
            place=request.POST['place']
            age=request.POST['age']
            mobile=request.POST['mobile']
            email=request.POST['email']
            password=request.POST['password']
            cat=request.POST['cat']
            dep=request.POST['dep']
            joindate=request.POST['date']
            exp=request.POST['exp']
            address=request.POST['address']
            obj1=staffadd(staffid=staffid,fname=fname,lname=lname,place=place,mobile=mobile,age=age,email=email,password=password,department_id=dep,staffcat_id=cat,address=address,experience=exp,joindate=joindate,status=1)
            obj1.save()
            return render(request,'addstaff.html',{'msg':'added successfully'})
    except Exception as e:print(e)
    return render(request,'addstaff.html',{'msg':'error'})

def Contactqueries(request):
    obj=patientqueries.objects.all()
  
    return render(request,'queries.html',{'query': obj})

def Opschedule(request):
    obj=doctoradd.objects.all()
  
    return render(request,'schedule.html',{'doc':obj})

def doctorschedule(request):
    if request.method=="POST":
        docid=request.POST['doctorid']
        docexist=dropschedule.objects.filter(doctorid_id=docid).exists()
        
        if docexist==False:
            day=request.POST.getlist('day')
            for i in day:
                day1=i
                dropschedule(doctorid_id=docid,day=i).save()
            start=request.POST['start']
            end=request.POST['end']
            pertime=request.POST['perpatient']
            doctortimings(doctorid_id=docid,start=start,end=end,pertime=pertime).save()
                
        else:return render(request,'schedule.html',{'msg':"Dr OP already scheduled"})
#         
    return redirect(Opschedule)
        
    

# def doctorschedule(request):
#     if request.method=="POST":
#         docid=request.POST['doctorid']
#         print(docid)
#         monday=request.POST.get('monday', False)
#         tuesday=request.POST.get('tuesday', False)
#         wednesday=request.POST.get('wednesday', False)
#         thursday=request.POST.get('thursday', False)
#         friday=request.POST.get('friday', False)
#         saturday=request.POST.get('saturday', False)
#         sunday=request.POST.get('sunday', False)
#         start=docid=request.POST['start']
#         end=docid=request.POST['end']
#         pertime=docid=request.POST['perpatient']
#         obj=doctorop(doctorid_id=docid,monday=monday,tuesday=tuesday,wednesday=wednesday,thursday=thursday,friday=friday,saturday=saturday,sunday=sunday)
#         obj.save()
#         obj2=doctortimings(doctorid_id=docid,start=start,end=end,perpatient=pertime)
#         obj2.save()
#         return render(request,'schedule.html',{'msg':"inserted successfully"})

def fnlogout(request):
    del request.session['admin']
    return render(request,'login.html')

def fndeletestaff(request,staff_id):
    obj=staffadd.objects.filter(id=staff_id)
    obj.update(status=0)
    return redirect(fnstaff)

def fnupdatestaff(request,updstaff_id):
    obj=staffadd.objects.filter(id=updstaff_id)
    obj1=staffcatogory.objects.all()
    obj2=departmentAdd.objects.all()
    return render(request,'updatestaff.html',{'staff':obj,'staffcat':obj1,'dep':obj2})

#update catogory
def fnupdatecatogory(request,updcat_id):
    obj=staffcatogory.objects.filter(id=updcat_id)
    return render(request,"addstaffcat.html",{'cat':obj})





   


