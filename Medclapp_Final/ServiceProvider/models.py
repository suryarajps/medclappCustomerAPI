from django.db import models
import datetime

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
from Admin_Section.models import Department,Category
import requests
from django.conf import settings
# class Category(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=120,unique=True)

    is_admin = models.BooleanField(default=False)
    is_serviceprovider = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone']

    def __str__(self):
        return self.email
    

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    # def get_serviceprovider(self):
    #     serviceprovider_profile=None
    #     if hasattr(self,'ProfileCompletion'):
    #         serviceprovider_profile=self.ProfileCompletion
    #     return serviceprovider_profile

    objects = CustomUserManager()


# class Service(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name

class Doctor(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.EmailField(default=None)
    departments = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    specialisation = models.CharField(max_length=120,default=None)
    photo = models.ImageField(upload_to='images',default=None)
    phone = models.CharField(max_length=120,default=None)
    organisation = models.CharField(max_length=120,default=None)

    def __str__(self):
        return self.fullname

class ProfileCompletion(models.Model):
    fullname = models.CharField(max_length=120,default=None)
    address = models.CharField(max_length=120,default=None)
    location = models.CharField(max_length=120,default=None)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL, blank=True, null=True)
    user=models.CharField(max_length=120)
    coverpicture = models.ImageField(upload_to='images',default=None)
    photo = models.ImageField(upload_to='images',default=None)
    departments = models.ForeignKey(Department, on_delete=models.SET_NULL, blank=True, null=True)
    bed_numbers = models.CharField(max_length=120,default=20)
    
    def __str__(self):
        return self.fullname


class Userprofile(models.Model):
    
    
    def __str__(self):
        return str(self.departments)

