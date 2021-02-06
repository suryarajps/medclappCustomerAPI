from django.forms import ModelForm
from django import forms
from Admin_Section.models import Category,Department,Advertisement
from Customer.models import CustomerProfile     
class Categoryform(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
        widgets = {
            'dept_name' : forms.TextInput(attrs={'class' : 'form-control'})

        }

class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisement
        fields = "__all__"
        widgets = {
            'advert_name' : forms.TextInput(attrs={'class' : 'form-control'})
            
        }

class CustomerAddForm(ModelForm):
    class Meta:
        model =  CustomerProfile  
        fields = "__all__"
        widegts = {
            'user' : forms.TextInput(attrs={'class': 'form-control'}),
            'fullname' : forms.TextInput(attrs={'class': 'form-control'}),
            'bloodgroup': forms.TextInput(attrs={'class': 'form-control'}),
            'gender' : forms.TextInput(attrs={'class': 'form-control'}),
            'dOB' : forms.TextInput(attrs={'class': 'form-control'}),
           'height' : forms.TextInput(attrs={'class': 'form-control'}),
            'weight' : forms.TextInput(attrs={'class': 'form-control'})           
        }