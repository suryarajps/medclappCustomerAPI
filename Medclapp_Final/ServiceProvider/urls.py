from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Doctorcreate,home,Doctoredit,Profilecreate,ProfileListing,password_success,PasswordsChangeView,ActivateAccountView,SetNewPasswordView,RequestResetEmailView,DeleteDoctor,Doctorlist,servicelisting,Deletservice,servicingedit,categorydelete,Createservice,Categoryedit,Categorylist,loginpage,registeration,logoutt,base

urlpatterns = [
    path('password/',PasswordsChangeView.as_view(template_name='ServiceProvider/change-password.html'),name="PasswordsChangeView"),
    path('password_success',password_success,name="password_success"),
    path('ProfileCreation',Profilecreate.as_view(),name="Profilecreate"),
    path('profilelisting',ProfileListing.as_view(),name="ProfileListing"),
    path('doctorcreate',Doctorcreate.as_view(),name="Doctorcreate"),
    path('doctorlist',Doctorlist.as_view(),name="Doctorlist"),
    path('doctoredit<int:pk>/',Doctoredit.as_view(),name="Doctoredit"),
    path('deletdoctor<int:pk>/',DeleteDoctor.as_view(),name="DeleteDoctor"),
    path('servicecreate',Createservice.as_view(),name="Createservice"),
    path('servicelisting',servicelisting.as_view(),name="servicelisting"),
    path('serviceedit<int:pk>',servicingedit.as_view(),name="servicingedit"),
    path('deleteservice<int:pk>',Deletservice.as_view(),name="Deletservice"),
    path('categorylist',Categorylist.as_view(),name="Categorylist"),
    path('Categoedit<int:pk>',Categoryedit.as_view(),name="Categoryedit"),
    path('categorydelete<int:pk>',categorydelete.as_view(),name="categorydelete"),
    path('register/', registeration.as_view(), name="register"),
    path('login', loginpage.as_view(), name="loginpage"),
    path('logout', logoutt.as_view(), name='logout'),
    path('base/', base.as_view(), name="base"),
    path('dashboard<int:pk>/',home,name="home"),
    path('activate/<uidb64>/<token>',ActivateAccountView.as_view(),name="activate"),
    path('set-new-password/<uidb64>/<token>',SetNewPasswordView.as_view(),name="set-new-password"),
    path('request-reset-email',RequestResetEmailView.as_view(),name="request-reset-email"),
]