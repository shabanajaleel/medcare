from django.db import models

class patientqueries(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    messsage=models.TextField()
