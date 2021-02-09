from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from ServiceProvider.forms import DoctorForm,ServiceForm,LoginForm,CategoryForm,ProfileCompletionForm,CustomUserCreationForm
from ServiceProvider.models import CustomUser,Doctor,ProfileCompletion
from Admin_Section.models import Category,Department
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import TemplateView,DeleteView,CreateView,ListView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib import messages
from django.template import RequestContext
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from ServiceProvider.utils import generate_token
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import random
from django.core.validators import validate_email
from django.contrib.auth.views import PasswordChangeView
from ServiceProvider.backends import CustomerBackend
from Customer.models import Request
# from Customer.forms import CustomUserCreationForm



#Profile listing
class Profilecreate(CreateView):
    model = ProfileCompletion
    form_class = ProfileCompletionForm
    template_name = "../templates/ServiceProvider/profilecreate.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = ProfileCompletionForm(data=request.POST,files=request.FILES)
        print(request.user)
        if form.is_valid():
            print('sucess')
            profile = form.save(commit=False)
            profile.user = request.user           
            profile.save()
            return redirect('base')
        else:
            print("form none")
            return redirect('Profilecreate')

#Profile Listing
class ProfileListing(ListView):
    template_name = "../templates/ServiceProvider/ProfileListing.html"
    model = ProfileCompletion
    form_class = ProfileCompletionForm
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.form_class
        qs=ProfileCompletion.objects.filter(user=request.user)
        self.context['doc']=qs
        return render(request, self.template_name, self.context)

#userprofile
# class Usercreate(CreateView):
#     model = Userprofile
#     form_class = UserprofileForm
#     template_name = "../templates/ServiceProvider/profile_section.html"
#     context = {}

#     def get(self, request, *args, **kwargs):
#         obj=ProfileCompletion.objects.get(user=request.user.email)
#         self.context['form'] = self.form_class(initial={'organisation':obj.fullname})
#         return render(request, self.template_name, self.context)

#     def post(self, request, *args, **kwargs):
#         form = UserprofileForm(data = request.POST, files = request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('loginpage')
#         else:
#             return render(request, self.template_name, self.context)

#user profile listing
# class UserProfilelist(TemplateView):
#     template_name = "../templates/ServiceProvider/categorylist.html"
#     model = Userprofile
#     form_class = UserprofileForm
#     context = {}

#     def querySet(self):
#         return self.model.objects.all()

#     def get(self, request, *args, **kwargs):
#         self.context['forms'] = self.querySet()
#         return render(request, self.template_name, self.context)

#user profile edit


class Categorylist(TemplateView):
    template_name = "../templates/ServiceProvider/categorylist.html"
    model = Category
    form_class = CategoryForm
    context = {}

    def querySet(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.querySet()
        return render(request, self.template_name, self.context)

class Categoryedit(TemplateView):
    model = Category
    form_class = CategoryForm()
    template_name = "../templates/ServiceProvider/categoryedit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = CategoryForm(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = CategoryForm(instance=qs, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Categorylist')
        else:
            return render(request, self.template_name, self.context)

class categorydelete(DeleteView):
    model = Category
    template_name = "../templates/ServiceProvider/categorydelete.html"
    form_class = CategoryForm
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = CategoryForm(instance=qs)
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        qs.delete()
        return redirect('Categorylist') 
#END category section

#ADDING SERVICES
class Createservice(CreateView):
    model = Department
    form_class = ServiceForm
    template_name = "../templates/ServiceProvider/service.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicelisting')
        else:
            return render(request, self.template_name, self.context)

#LISTING SERVICES
class servicelisting(TemplateView):
    template_name = "../templates/ServiceProvider/servicelisting.html"
    model = Department
    form_class = ServiceForm
    context = {}

    def querySet(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.querySet()
        return render(request, self.template_name, self.context)

#EDITING SERVICES
class servicingedit(TemplateView):
    model = Department
    form_class = ServiceForm()
    template_name = "../templates/ServiceProvider/serviceedit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = ServiceForm(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = ServiceForm(instance=qs, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('servicelisting')
        else:
            return render(request, self.template_name, self.context)

#DELETING SERVICES

class Deletservice(DeleteView):
    model = Department
    template_name = "../templates/ServiceProvider/deleteservice.html"
    form_class = ServiceForm
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = ServiceForm(instance=qs)
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        qs.delete()
        return redirect('servicelist') 
#ended Servce section

#Doctor add section
class Doctorcreate(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = "../templates/ServiceProvider/AddDoctor.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = DoctorForm(data=request.POST,files=request.FILES)
        print(request.user)
        if form.is_valid():
            print('sucess')
            profile = form.save(commit=False)
            profile.organisation = request.user           
            profile.save()
            return redirect('base')
        else:
            print("form none")
            return redirect('Doctorcreate')

#doctor listing
class Doctorlist(ListView):
    template_name = "../templates/ServiceProvider/doctorlist.html"
    model = Doctor
    form_class = DoctorForm
    context = {}
    
    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.form_class
        qs=Doctor.objects.filter(organisation=request.user)
        self.context['doc']=qs
        return render(request, self.template_name, self.context)

#doctor edit 
class Doctoredit(TemplateView):
    model = Doctor
    form_class = DoctorForm
    template_name = "../templates/ServiceProvider/DoctorEdit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = DoctorForm(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = DoctorForm(instance=qs, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Doctorlist')
        else:
            return render(request, self.template_name, self.context)

#Doctor delete details
class DeleteDoctor(DeleteView):
    model = Doctor
    template_name = "../templates/ServiceProvider/DoctorDelete.html"
    form_class = DoctorForm
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = DoctorForm(instance=qs)
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        qs.delete()
        return redirect('Doctorlist') 

#end doctor section



#blood request section
def home(request):
    qs=Request.objects.all()
    context={"Edit":qs}
    return render(request,'../templates/ServiceProvider/status.html',context)
# def Landing(request):
#     return render(request, "ServiceProvider/index.html")


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request,'../templates/ServiceProvider/password_success.html',)



class base(TemplateView):
    template_name = "../templates/ServiceProvider/base.html"
    model = CustomUser
    context = {}

    def querySet(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.querySet()
        return render(request, self.template_name, self.context)        

class registeration(TemplateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = "../templates/ServiceProvider/register.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class()
        return render(request, self.template_name, self.context)
    

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(data = request.POST, files=request.FILES )
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(request,"Your Registration is success")
            current_site = get_current_site(request)
            email_subject = '[ACtive Your Account]',
            message = render_to_string('../templates/ServiceProvider/active.html',
            {
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':generate_token.make_token(user)
            }
            )
            email_message = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email]
            )
            email_message.send()
            return redirect("loginpage")
        else:
            self.context['form'] = self.form_class
            print(form)
            return render(request, self.template_name, self.context)

class loginpage(TemplateView):
    model = CustomUser
    form_class = LoginForm
    template_name = "../templates/ServiceProvider/loginpage.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        # print(uname)
        # print(email,",",password)
        user = authenticate(email=email, password=password)
        # print(user)
        if user is not None:
            login(request, user)
            print("success")
            if user.is_authenticated:
                print("uni")
                obj1=ProfileCompletion.objects.all()
                print(obj1)
                if obj1.exists():
                    for datas in obj1:
                        if request.user==datas.user:
                            print('yes')
                            return redirect('base')
                        else:
                            return redirect('Profilecreate')  

                else: 
                    # if request.user.email != datas.user:
                        print('no')
                        return redirect('Profilecreate')           
        else:
            print("failed")



class ActivateAccountView(TemplateView):
    def get(self,request,uidb64,token):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user=CustomUser.objects.get(pk=uid)
        except Exception as identifier:
            user=None
        
        if user is not None and generate_token.check_token(user,token):
            user.is_active=True
            user.save()
            messages.add_message(request,messages.INFO,'account activated successfully')
            return redirect('loginpage') 
        return render(request,'../templates/ServiceProvider/active_failed.html',status=401)

class logoutt(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('loginpage')

class RequestResetEmailView(TemplateView):
    def get(self,request):
        return render(request,'../templates/ServiceProvider/request-reset-email.html')
    
    def post (self,request):
        email=request.POST['email']


        if not validate_email(email):
            messages.error(request,"please enter a valid email")
            return render(request,"../templates/ServiceProvider/request-reset-email.html")

        
        user = CustomUser.objects.filter(email=email)

        if user.exists():
            current_site = get_current_site(request)
            email_subject = '[Reset your Password]',
            message = render_to_string('../templates/ServiceProvider/reset-user-password.html',
            {
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user[0].pk)),
                'token': PasswordResetTokenGenerator().make_token(user[0])
            }
            )
            email_message = EmailMessage(
            email_subject,
            message,
            settings.EMAIL_HOST_USER,
            [email]
            )
            email_message.send()

        messages.success(
            request,"we have sent you have an email with instructions on how to reset your password ")
        
        return render(request,"../templates/ServiceProvider/request-reset-email.html")


class  SetNewPasswordView(TemplateView):
    model = CustomUser
    form_class = CustomUserCreationForm
   

    def get(self, request, uidb64, token):
        context={
            'uidb64':uidb64,
            'token':token
        }
        return render(request,"../templates/ServiceProvider/set-new-password.html",context)
    def post(self, request, uidb64, token):
        context={
            'uidb64':uidb64,
            'token':token,
            'has_error':False
        }
        password = request.POST.get('password1')
        password2=request.POST.get('password2')
        if len(password) < 6:

            print('passwords should be at least 6 characters long')
            context['has_error'] = True
        if password != password2:
            print('passwords don`t match')
            context['has_error'] = True

        if context['has_error'] == True:
            return render(request, '../templates/ServiceProvider/set-new-password.html', context)

        try:
            user_id = force_text(urlsafe_base64_decode(uidb64))
            user=CustomUser.objects.get(pk=user_id)
            user.set_password(password)
            user.save()

            print('Password reset success,your can login with new password')

            return redirect('loginpage')
        except DjangoUnicodeDecodeError as identifier:
            messages.error(request,"something went wrong")
            return render(request,"../templates/ServiceProvider/request-reset-email.html",context)



        return render(request,"../templates/ServiceProvider/request-reset-email.html",context)





            

