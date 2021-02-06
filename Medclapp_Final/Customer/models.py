from django.db import models
import datetime
from ServiceProvider.models import CustomUser
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomerProfile(models.Model):
    user = models.CharField(max_length=100)
    fullname = models.CharField(max_length=120,unique=True)
    choice = (
        ('AB+ve','AB+ve'),
        ('A+ve','A+ve'),
        ('B+ve','B+ve'),
        ('O+ve','O+ve'),
        ('AB-ve','AB-ve'),
        ('A-ve','A-ve'),
        ('B-ve','B-ve'),
        ('O-ve','O-ve'),
    )
    bloodgroup = models.CharField(max_length=100,choices=choice)
    choicea = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    gender = models.CharField(max_length=100,choices=choicea)
    dOB = models.DateField(blank=False,null=True)
    height = models.CharField(max_length=10)
    weight = models.CharField(max_length=10)
    address = models.CharField(max_length=10)
    profilepicture = models.ImageField(upload_to='images',default=None)


class Request(models.Model):
    user = models.CharField(max_length=100)
    choiceb = (
        ('A+','A+'),
        ('B+','B+'),
        ('AB+','AB+'),
        ('O+','O+'),
        ('A-','A-'),
        ('B-','B-'),
        ('AB-','AB-'),
        ('O-','O-'),
    )
    bloodgrouprequest = models.CharField(max_length=100,choices=choiceb)
    patientname = models.CharField(max_length=50)
    age = models.CharField(max_length=3)
    location = models.TextField(max_length=250)
    phonenumber = models.CharField(max_length=15)
    date = models.DateField(default=datetime.date.today(),blank=False)
    time = models.TimeField(blank=False)
    choiceb = (
        ('Within 1 Hour','Within 1 Hour'),
        ('Within 6 Hours','Within 6 Hours'),
        ('Within 12 Hours','Within 12 Hours'),
        ('Within 24 Hours','Within 24 Hours'),
    )
    priority = models.CharField(max_length=100,choices=choiceb)
    

    def __str__(self):
        return self.priority



class Familymembers(models.Model):
    user = models.CharField(max_length=100)
    fullname = models.CharField(max_length=50)
    choicec = (
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    )
    gender = models.CharField(max_length=100,choices=choicec)
    dob = models.DateField(blank=False)
    relationship = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    

    def __str__(self):
        return self.fullname
    


class Medicalrecords(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today(),blank=False)
    detail = models.CharField(max_length=200)
    file = models.FileField(upload_to='images')
    #add user field
    
    def __str__(self):
        return self.detail

