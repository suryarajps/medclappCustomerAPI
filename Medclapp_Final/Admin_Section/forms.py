from django.forms import ModelForm
from django import forms
from Admin_Section.models import Category,Department,Advertisement,Service,Blog
from Customer.models import CustomerProfile   
from ServiceProvider.models import Doctor

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

class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"
        widgets = {
            'service_name' : forms.TextInput(attrs={'class' : 'form-control'})
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
            'user' : forms.TextInput(attrs={'class' : 'form-control'}),
            'fullname' : forms.TextInput(attrs={'class' : 'form-control'}),
            # 'bloodgroup': forms.TextInput(attrs={'class' : 'form-control'}),
            # 'gender' : forms.TextInput(attrs={'class' : 'form-control'}),
            'dOB' : forms.DateInput(attrs={'class' : 'form-control'}),
            'height' : forms.TextInput(attrs={'class' : 'form-control'}),
            'weight' : forms.TextInput(attrs={'class' : 'form-control'}),        
        }

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = "__all__"
        widegts = {
            'blog_title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'blog_description' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields=('fullname','email','departments','specialisation','photo','phone','organisation')
        widgets = {
            "fullname": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "specialisation": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }