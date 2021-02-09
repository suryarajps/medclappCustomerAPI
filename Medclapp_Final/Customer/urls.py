
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from Customer.views import loginn,registeration,logoutt,Userdetails,Index,Requestcreate,Bloodrequests,Familymembercreate,Familymembersdetails,Customerprofilecreate,Passwordchange,Passwordresetdone

urlpatterns = [
    path('', registeration.as_view(), name="customerregister"),
    path('login/', loginn.as_view(), name="loginn"),
    path('logout', logoutt.as_view(), name='logoutt'),
    path('userprofile/', Userdetails.as_view(), name='userprofile'),
    path('index/', Index.as_view(), name='index'),
    path('requestcreate/',Requestcreate.as_view(), name="requestcreate"),
    path('requestlist/',Bloodrequests.as_view(), name="requestlist"),
    path('familymembercreate/',Familymembercreate.as_view(), name="familymembercreate"),
    path('familymemberdetails/', Familymembersdetails.as_view(), name='familymemberdetails'),
    path('customerprofilecreate/',Customerprofilecreate.as_view(), name="customerprofilecreate"),
    path('changepassword/',Passwordchange.as_view(),name="passwordchange"),
    path('resetpassword/',Passwordresetdone.as_view(),name="passwordreset"),
    
]