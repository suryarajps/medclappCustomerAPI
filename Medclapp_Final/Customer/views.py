from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from Customer.forms import LoginForm,CustomUserCreationForm,CustomUserChangeForm,Requestform,Familymemberform,Medicalrecordsform,Customerprofileform
from Customer.models import Request,Familymembers,Medicalrecords,CustomerProfile
from ServiceProvider.models import CustomUser
from django.views.generic import TemplateView,CreateView
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from Customer.backends import CustomerBackend



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
        phone = request.POST.get('phone') # take email in form for username
        password = request.POST.get('password')
        print(phone,",",password)
        obj = CustomUser.objects.get(phone=phone)
        print (obj.email)
        user = authenticate(email=obj.email, password=password,backend='Customer.backends.CustomerBackend')
        print('inside user')
        if user is not None:
            login(request, user)
            print("success")
            return redirect('customerprofilecreate')
        else:
            print("failed")
        #     print("success")
        #     obj=CustomerProfile.objects.get(user=request.user.email)
        #     if(request.user.email==obj.user):
        #         return redirect('index')
        #     else:
        #         return redirect('customerprofilecreate')
        # else:
        #     print("failed")



class logoutt(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('loginn')



class Userdetails(TemplateView):
    context = {}
    def get(self, request):
        obj = CustomerProfile.objects.get(user=request.user.email)
        self.context['data']= obj
        return render(request,"../templates/Customer/myprofile.html",self.context)



class Index(TemplateView):
    context = {}
    def get(self, request):
        obj = CustomerProfile.objects.get(user=request.user.email)
        self.context['data']= obj
        return render(request,"../templates/Customer/index.html",self.context)



class Requestcreate(CreateView):
    model = Request
    form_class = Requestform()
    template_name = "../templates/Customer/requestcreate.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class(initial={'user': request.user.email})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = Requestform(data = request.POST,files = request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('requestcreate')




class Bloodrequests(TemplateView):
    template_name = "../templates/Customer/requestview.html"
    model = Request
    context = {}

    def querySet(self,request):
        return self.model.objects.all().exclude(user=request.user)


    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.querySet()
        return render(request, self.template_name, self.context)



class Familymembercreate(CreateView):
    model = Familymembers
    form_class = Familymemberform()
    template_name = "../templates/Customer/familymembercreate.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class(initial={'user': request.user.email})
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = Familymemberform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('familymembercreate')        




class Familymembersdetails(TemplateView):
    template_name = "../templates/Customer/familymemberdetails.html"
    model = Familymembers
    context = {}

    def querySet(self,request):
        return self.model.objects.get(user=request.user.email)

    # def querySet(self,request):
    #     obj = CustomerProfile.objects.get(user=request.user.email)
    #     self.context['data']= obj
    #     return self.model.objects.filter(user='user')   

    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.querySet()
        return render(request, self.template_name, self.context)        




def Medicalrecordscreate(request):
    context={}
    context['form'] = Medicalrecordsform(initial={'user': request.user.email})

    if request.method == "POST":
        form = Medicalrecordsform(request.POST, request.FILES)
        files = request.FILES.getlist('file')
        if form.is_valid():
            for f in files:
                file_instance = Medicalrecords(file=f)
                file_instance.save()
        return redirect('index')
    else:
        form = Medicalrecordsform()
    return render(request, '../templates/Customer/medicalrecordscreate.html', context)



class Medicalrecordsdetails(TemplateView):
    template_name = "../templates/Customer/medicalrecordsview.html"
    model = Medicalrecords
    context = {}
    
    def querySet(self,request):
        return self.model.objects.filter(user=request.user.email)

    def get(self, request, *args, **kwargs):
        self.context['forms'] = self.querySet()
        return render(request, self.template_name, self.context)    



class Customerprofilecreate(CreateView):
    model = CustomerProfile
    form_class = Customerprofileform
    template_name = "../templates/Customer/customerprofile.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class(initial={'user': request.user.email})
        return render(request, self.template_name, self.context)


    def post(self, request, *args, **kwargs):
        form = Customerprofileform(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return redirect('customerprofilecreate')         
                      