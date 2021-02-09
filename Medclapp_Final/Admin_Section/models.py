from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40,unique=True)

    def __str__(self):
        return self.name

class Department(models.Model):
    dept_name = models.CharField(max_length=40)
    category_name = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self): 
        return self.dept_name

class Advertisement(models.Model):
    advert_name = models.CharField(max_length=120)
    advert_photo = models.ImageField(upload_to='images',default=None)

class Service(models.Model):
    service_name = models.CharField(max_length=40,unique=True)
    category_name = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

class Blog(models.Model):
    blog_title = models.CharField(max_length=40)
    blog_description = models.TextField()
    blog_image = models.ImageField(upload_to='images',default=None)