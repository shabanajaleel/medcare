from django.db import models
from django.db.models.deletion import CASCADE
from hmsadmin.models import doctoradd,departmentAdd,dropschedule

# Create your models here.
#patient appointment model

class appointments(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    age=models.IntegerField()
    mobile=models.BigIntegerField()
    address=models.TextField()
    dep=models.ForeignKey(departmentAdd,on_delete=CASCADE)
    doc=models.ForeignKey(doctoradd,on_delete=CASCADE)
    day=models.ForeignKey(dropschedule,on_delete=CASCADE)
    status=models.IntegerField()

