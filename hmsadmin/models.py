from random import expovariate
from django.db import models
from django.db.models.deletion import CASCADE
import datetime


class AdminRegister(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=25)

class departmentAdd(models.Model):
    depname=models.CharField(max_length=30)
    imagefile=models.CharField(max_length=100)
    description=models.TextField()

class staffcatogory(models.Model):
    catogoryname=models.CharField(max_length=30)

class staffadd(models.Model):
    staffid=models.CharField(max_length=20)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=30)
    staffcat=models.ForeignKey(staffcatogory,on_delete=CASCADE)
    department=models.ForeignKey(departmentAdd,on_delete=CASCADE)
    joindate=models.DateField()
    experience=models.CharField(max_length=30)
    address=models.TextField()
    status=models.IntegerField(default=None)

class doctoradd(models.Model):
    docid=models.CharField(max_length=20)
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=30)
    quali=models.CharField(max_length=30,blank=True)
    department=models.ForeignKey(departmentAdd,on_delete=CASCADE)
    imagefile=models.CharField(max_length=100)
    joindate=models.DateField()
    experience=models.IntegerField()
    address=models.TextField()
    description=models.TextField()
    status=models.IntegerField(default=None)

class doctorop(models.Model):
    doctorid=models.ForeignKey(doctoradd,on_delete=CASCADE)
    monday=models.IntegerField(blank=True)
    tuesday=models.IntegerField(blank=True)
    wednesday=models.IntegerField(blank=True)
    thursday=models.IntegerField(blank=True)
    friday=models.IntegerField(blank=True)
    saturday=models.IntegerField(blank=True)
    sunday=models.IntegerField(blank=True)

class doctortimings(models.Model):
    doctorid=models.ForeignKey(doctoradd,on_delete=CASCADE)
    start=models.TimeField(default=datetime.time(16, 00))
    end=models.TimeField(default=datetime.time(16, 00))
    pertime=models.CharField(max_length=30,default=True)

class dropschedule(models.Model):
    doctorid=models.ForeignKey(doctoradd,on_delete=CASCADE)
    day=models.CharField(max_length=30,default=True,blank=True)









