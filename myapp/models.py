from django.db import models

# Create your models here.

class Notice(models.Model):
    dpt = models.CharField(max_length=100)
    acayear = models.IntegerField()
    expdate = models.CharField(max_length=100)
    topic = models.CharField(max_length=250)
    content = models.TextField()


class Student(models.Model):
    regno = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dpt = models.CharField(max_length=100)
    acayear = models.IntegerField(default=1)
    funq = models.CharField(max_length=200)
   

class UImage(models.Model):
    uindex = models.CharField(max_length=30)
    imgname = models.CharField(max_length=100)
