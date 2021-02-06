from django import forms
from django.forms import ModelForm
from ServiceProvider.models import Userprofile,CustomUser,Doctor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Admin_Section.models import Department,Category
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from ServiceProvider.models import CustomUser,Userprofile,ProfileCompletion,Doctor


class ProfileCompletionForm(ModelForm):
    class Meta(UserCreationForm):
        model = ProfileCompletion
        fields = ('fullname','address','location','category','user')
        widgets = {
            "fullname": forms.TextInput(attrs={"class": "form-control"}),
            "address": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "user": forms.TextInput(attrs={"class": "form-control"}),
        } 


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields='__all__'

class UserprofileForm(ModelForm):
    class Meta:
        model = Userprofile
        fields='__all__'

class ServiceForm(ModelForm):
    class Meta:
        model = Department
        fields='__all__'

class DoctorForm(forms.ModelForm):
    class Meta(UserCreationForm):
        model = Doctor
        fields='__all__'



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','phone')
        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.TextInput(attrs={"class": "form-control"}),
        }      

# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = CustomUser
#         fields = ('phone','email')
#         widgets = {
#             'phone': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
           
#         }


#end          


class LoginForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email','password')
        widgets = {
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }  

