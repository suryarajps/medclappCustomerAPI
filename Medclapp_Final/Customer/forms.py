from django import forms
from django.forms import ModelForm
from Customer.models import Request,Familymembers,CustomerProfile
from ServiceProvider.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class DateInput(forms.DateInput):
        input_type = 'date'

class Customerprofileform(ModelForm):

    class Meta:
        model = CustomerProfile
        fields = ('fullname','bloodgroup','gender','dOB','height','weight','profilepicture','address')
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'dOB' : DateInput(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('phone','email')
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
           
        }

#profile form 

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('phone','password')

# class LoginForm(forms.Form):
#     phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class LoginForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('phone','password')
        widgets = {
            "phone": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }  

class TimeInput(forms.TimeInput):
        input_type = 'time'

class Requestform(ModelForm):
    class Meta:
        model = Request
        fields = ('bloodgrouprequest','patientname','age','location','phonenumber','date','time')
        widgets = {
            'patientname': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'date' : DateInput(attrs={'class': 'form-control'}),
            'time' : TimeInput(attrs={'class': 'form-control'}),
        }   


class Familymemberform(ModelForm):
    class Meta:
        model = Familymembers
        fields = ('fullname','gender','dob','relationship','phone')
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'form-control'}),
            'dob' : DateInput(attrs={'class': 'form-control'}),
            'relationship': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
        }           
