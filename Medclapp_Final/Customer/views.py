from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView
from django.urls import reverse_lazy

from Customer.forms import LoginForm,CustomUserCreationForm,CustomUserChangeForm,Requestform,Familymemberform,Customerprofileform
from Customer.models import Request,Familymembers,CustomerProfile
from ServiceProvider.models import CustomUser
from django.views.generic import TemplateView,CreateView,ListView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from Customer.backends import CustomerBackend
# from ServiceProvider.models import ProfileCompletion,Doctor
from Admin_Section.models import Category
from ServiceProvider.forms import CategoryForm



class registeration(TemplateView):
    model = CustomUser
    form_class = CustomUserCreationForm()
    template_name = "../templates/Customer/customerregister.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(data = request.POST, files=request.FILES )
        if form.is_valid():
            form.save()
            return redirect("loginn")
        else:
            self.context['form'] = self.form_class
            return render(request, self.template_name, self.context)



class loginn(TemplateView):
    model = CustomUser
    form_class = LoginForm
    template_name = "../templates/Customer/loginn.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    # def post(self, request, *args, **kwargs):
    #     form = LoginForm(request.POST)
    #     phone = request.POST.get('phone', False)
    #     password = request.POST.get('password', False)
    #     # print(uname)
    #     # print(email,",",password)
    #     user = CustomerBackend(phone=phone, password=password,backend='ServiceProvider.backends.CustomerBackend')
    #     # print(user)
    #     if user is not None:
    #         login(request, user)
    #         print("success")
    #         return redirect('index')
    #     else:
    #         print('login failed')
    #         return redirect('loginn')

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        print('inside post')
        # if form.is_valid():
        print('inside form')
        phone = request.POST.get('phone') 
        password = request.POST.get('password')
        print(phone,",",password)
        obj = CustomUser.objects.get(phone=phone)
        print (obj.email)
        user = authenticate(email=obj.email, password=password,backend='Customer.backends.CustomerBackend')
        print('inside user')
        if user is not None:
            login(request, user)
            print("success")
            print(obj.email)
            if user.is_authenticated:
                print("uni")
                obj1=CustomerProfile.objects.all()
                print(obj1)
                if obj1.exists():
                    for datas in obj1:
                        # print('k',datas.user)
                        # print(request.user)
                        if request.user==datas.user:
                            print('yes')
                            return redirect('index')
                        else:
                            return redirect('customerprofilecreate')  

                else: 
                    # if request.user.email != datas.user:
                        print('no')
                        return redirect('customerprofilecreate')           
        else:
            print("failed")
        #     print("success")
        #     # obj=CustomerProfile.objects.get(user=request.user.email)
            
        #     if  not request.user.is_authenticated:
        #         return redirect('customerprofilecreate')
        #         print('sucess1')

        #     else:
        #         print('fail1')
        #         return redirect('index')
        # else:
        #     print("failed")



class logoutt(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('loginn')



class Userdetails(TemplateView):
    context = {}
    def get(self, request):
        obj = CustomerProfile.objects.get(user=request.user)
        self.context['data']= obj
        return render(request,"../templates/Customer/myprofile.html",self.context)



class Index(TemplateView):
    template_name = "../templates/Customer/index.html"
    model = Category
    form_class = CategoryForm
    context = {}

    def querySet(self):
         return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        obj = CustomerProfile.objects.get(user=request.user)
        self.context['data']= obj

        self.context['forms'] = self.querySet()
        return render(request, self.template_name, self.context)
        

        return render(request,"../templates/Customer/index.html")  



class Requestcreate(CreateView):
    model = Request
    form_class = Requestform
    template_name = "../templates/Customer/requestcreate.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class

        obj = CustomerProfile.objects.get(user=request.user)
        self.context['data']= obj
        
        return render(request, self.template_name, self.context)


    def post(self, request, *args, **kwargs):
        form = Requestform(data=request.POST,files=request.FILES)
        print(request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user           
            profile.save()
            return redirect('index')
        else:
            return redirect('requestcreate')  




class Bloodrequests(TemplateView):
    template_name = "../templates/Customer/requestview.html"
    model = Request
    form_class = Requestform
    context = {}


    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        qs = Request.objects.all()
        self.context['request']=qs

        obj = CustomerProfile.objects.get(user=request.user)
        self.context['data']= obj

        return render(request, self.template_name, self.context)



class Familymembercreate(CreateView):
    model = Familymembers
    form_class = Familymemberform
    template_name = "../templates/Customer/familymembercreate.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class

        obj = CustomerProfile.objects.get(user=request.user)
        self.context['data']= obj
        
        return render(request, self.template_name, self.context)


    def post(self, request, *args, **kwargs):
        form = Familymemberform(data=request.POST,files=request.FILES)
        print(request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user           
            profile.save()
            return redirect('index')
        else:
            return redirect('familymembercreate')       



class Familymembersdetails(TemplateView):
    template_name = "../templates/Customer/familymemberdetails.html"
    model = Familymembers
    form_class = Familymemberform
    context = {}

    # def querySet(self):
    #     return self.model.objects.get(user=request.user.email)

    # def querySet(self,request):
    #     obj = CustomerProfile.objects.get(user=request.user.email)
    #     self.context['data']= obj
    #     return self.model.objects.filter(user='user')   

    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.form_class
        qs = Familymembers.objects.filter(user=request.user)
        self.context['family']=qs

        obj = CustomerProfile.objects.get(user=request.user)
        self.context['data']= obj
        
        return render(request, self.template_name, self.context)        



class Customerprofilecreate(CreateView):
    model = CustomerProfile
    form_class = Customerprofileform
    template_name = "../templates/Customer/customerprofile.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)


    def post(self, request, *args, **kwargs):
        form = Customerprofileform(data=request.POST,files=request.FILES)
        print(request.user)
        if form.is_valid():
            print('sucess')
            profile = form.save(commit=False)
            profile.user = request.user           
            profile.save()
            return redirect('index')
        else:
            print("form none")
            return redirect('customerprofilecreate')         
                      
                  
class Passwordchange(PasswordChangeView):

    template_name = "../templates/Customer/passwordchange.html"
    success_url = reverse_lazy('passwordreset')

class Passwordresetdone(PasswordResetDoneView):
    
    template_name = "../templates/Customer/passwordresetdone.html"

