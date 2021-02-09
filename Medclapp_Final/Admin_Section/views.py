from django.shortcuts import render,redirect
from ServiceProvider.models import Doctor,CustomUser,ProfileCompletion
from Customer.models import Request,Familymembers,CustomerProfile
from Admin_Section.models import Category,Department,Advertisement,Service,Blog
from django.views.generic import TemplateView,DeleteView
from Customer.forms import CustomUserCreationForm,Requestform,Familymemberform
from ServiceProvider.forms import ProfileCompletionForm
from Admin_Section.forms import Categoryform,AdvertisementForm,DepartmentForm,CustomerAddForm,ServiceForm,BlogForm,DoctorForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request,"../templates/admin_section/dashboard.html")

class ServiceProviderList(TemplateView):
    template_name = "../templates/admin_section/serviceprovider_list.html"
    context = {}
    list2 = []
    def get(self,request,*awrgs,**kwargs):
        obj = ProfileCompletion.objects.all()
        list1=[]
        for datas in obj:
            query = datas.fullname,datas.category,datas.id

            list1.append(query)
        return render(request,self.template_name,{'form':list1})

class ServiceProviderService(TemplateView):
    template_name = "../templates/admin_section/serviceprovider_service.html"
    context = {}
    list2 = []
    def get(self,request,*awrgs,**kwargs):
        id = kwargs.get('pk')
        datas = ProfileCompletion.objects.filter(id=id)
        list1=[]
        # for datas in obj:
        query = datas.fullname,datas.category,datas.id,datas.department
        list1.append(query)
            # services = Userprofile.objects.filter(organization=datas.fullname)
            # for qs in services:              
            #     ls = qs.id,qs.departments,qs.category,qs.organization
            #     list1.append(ls)
        return render(request,self.template_name,{'form':list1})


class CustomerList(TemplateView):
    template_name = "../templates/admin_section/customer_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = CustomerProfile.objects.all()
        print(obj)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)

class CustomerDetail(TemplateView):
    template_name = "../templates/admin_section/customer_details.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = CustomerProfile.objects.all()
        print(obj)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)

class DoctorList(TemplateView):
    template_name = "../templates/admin_section/doctors_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = Doctor.objects.all()
        # for data in obj:
        #     print(data.fullname,data.category,data.service)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)

class CustomerAdd(TemplateView):
    template_name = "../templates/admin_section/customer_add.html"
    context = {}
    form_class = CustomerAddForm
    model = CustomerProfile

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self,request,*awrgs,**kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admincustomerlist')
        else:
            return redirect('admincustomeradd')

class CustomerEdit(TemplateView):
    model = CustomerProfile
    form_class = CustomerAddForm
    template_name = "../templates/admin_section/customer_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = CustomerAddForm(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = CustomerAddForm(instance=qs, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admincustomerlist')
        else:
            return render(request, self.template_name, self.context)

class CustomerView(TemplateView):
    model = CustomerProfile
    template_name = "../templates/admin_section/customer_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class CustomerDelete(DeleteView):
    model = CustomerProfile
    success_url = reverse_lazy("admincustomerlist")

class ProviderAdd(TemplateView):
    template_name = "../templates/admin_section/provider_add.html"
    context = {}
    form_class = ProfileCompletionForm
    model = ProfileCompletion

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self,request,*awrgs,**kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('providerlist')
        else:
            return redirect('provideradd')

class ProviderEdit(TemplateView):
    form_class = ProfileCompletionForm
    model = ProfileCompletion
    template_name = "../templates/admin_section/provider_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = CustomUserCreationForm(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = CustomUserCreationForm(instance=qs, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('providerlist')
        else:
            return render(request, self.template_name, self.context)

class ProviderView(TemplateView):
    model = CustomUser
    template_name = "../templates/admin_section/provider_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class ProviderDelete(DeleteView):
    model = CustomUser
    success_url = reverse_lazy("providerlist")

class ProviderList(TemplateView):
    template_name = "../templates/admin_section/provider_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = CustomUser.objects.all()
        print(obj)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)

class Requestcreate(TemplateView):
    model = Request
    form_class = Requestform
    template_name = "../templates/admin_section/request_create.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = Requestform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminindex')
        else:
            return redirect('create')

class Requestlist(TemplateView):
    template_name = "../templates/admin_section/request_list.html"
    model = Request
    context = {}

    def querySet(self):
        return self.model.objects.all()

    def get(self, request, *args, **kwargs):
        self.context['items'] = self.querySet()
        return render(request, self.template_name, self.context)   

class Requestedit(TemplateView):
    model = Request
    form_class = Requestform
    template_name = "../templates/admin_section/request_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = Requestform(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = Requestform(instance=qs, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminindex')
        else:
            return render(request, self.template_name, self.context)  

class Requestdelete(DeleteView):
    model = Request
    success_url = reverse_lazy("list")

class Requestview(TemplateView):
    model = Request
    template_name = "../templates/admin_section/request_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class BloodEmergency(TemplateView):
    model = Request
    template_name = "../templates/admin_section/blood_emergency.html"
    context = {}

    def get(self, request, *args, **kwargs):
        qs = self.model.objects.filter(priority="Within 1 Hour")
        self.context['form'] = qs
        return render(request, self.template_name, self.context)


class BloodModerate(TemplateView):
    model = Request
    template_name = "../templates/admin_section/blood_moderate.html"
    context = {}

    def get(self, request, *args, **kwargs):
        qs = self.model.objects.filter(priority="Within 6 Hours")
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class BloodNormal(TemplateView):
    model = Request
    template_name = "../templates/admin_section/blood_normal.html"
    context = {}

    def get(self, request, *args, **kwargs):
        qs = self.model.objects.filter(priority="Within 12 Hours")
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class BloodHour(TemplateView):
    model = Request
    template_name = "../templates/admin_section/blood_24hour.html"
    context = {}

    def get(self, request, *args, **kwargs):
        qs = self.model.objects.filter(priority="Within 24 Hours")
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class CategoryAdd(TemplateView):
    template_name = "../templates/admin_section/category_add.html"
    context = {}
    form_class = Categoryform
    model = Category

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self,request,*awrgs,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admincategorylist')
        else:
            return redirect('admincategoryadd')

class CategoryEdit(TemplateView):
    model = Category
    form_class = Categoryform
    template_name = "../templates/admin_section/category_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = Categoryform(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = Categoryform(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('admincategorylist')
        else:
            return render(request, self.template_name, self.context)

class CategoryView(TemplateView):
    model = Category
    template_name = "../templates/admin_section/category_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy("admincategorylist")

class CategoryList(TemplateView):
    template_name = "../templates/admin_section/category_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = Category.objects.all()
        print(obj)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)

class DepartmentAdd(TemplateView):
    template_name = "../templates/admin_section/department_add.html"
    context = {}
    form_class = DepartmentForm

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self,request,*awrgs,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admindepartmentlist')
        else:
            return redirect('admindepartmentadd')

class DepartmentEdit(TemplateView):
    model = Department
    form_class = DepartmentForm
    template_name = "../templates/admin_section/department_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = DepartmentForm(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = DepartmentForm(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('admindepartmentlist')
        else:
            return render(request, self.template_name, self.context)

class DepartmentView(TemplateView):
    model = Department
    template_name = "../templates/admin_section/department_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class DepartmentDelete(DeleteView):
    model = Department
    success_url = reverse_lazy("admindepartmentlist")

class DepartmentList(TemplateView):
    template_name = "../templates/admin_section/department_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = Department.objects.all()
        print(obj)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)

class AdvertisementAdd(TemplateView):
    template_name = "../templates/admin_section/advertisement_add.html"
    context = {}
    form_class = AdvertisementForm

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self,request,*awrgs,**kwargs):
        form = self.form_class(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adminadvertisementlist')
        else:
            return redirect('adminadvertisementadd')

class AdvertisementEdit(TemplateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = "../templates/admin_section/advertisement_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = AdvertisementForm(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminadvertisementlist')
        else:
            return render(request, self.template_name, self.context)

class AdvertisementView(TemplateView):
    model = Advertisement
    template_name = "../templates/admin_section/advertisement_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class AdvertisementDelete(DeleteView):
    model = Advertisement
    success_url = reverse_lazy("adminadvertisementlist")

class AdvertisementList(TemplateView):
    template_name = "../templates/admin_section/advertisement_list.html"
    context = {}
    model = Advertisement

    def get(self,request,*awrgs,**kwargs):
        obj = self.model.objects.all()
        print(obj)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)


class FamilyMembersAdd(TemplateView):
    template_name = "../templates/admin_section/familymembers_add.html"
    context = {}
    form_class = Familymemberform

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self,request,*awrgs,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminfamilylist')
        else:
            return redirect('adminfamilyadd')

class FamilyMembersEdit(TemplateView):
    model = Familymembers
    form_class = Familymemberform
    template_name = "../templates/admin_section/familymembers_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = Familymemberform(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = Familymemberform(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminfamilylist')
        else:
            return render(request, self.template_name, self.context)

class FamilyMembersView(TemplateView):
    model = Familymembers
    template_name = "../templates/admin_section/familymembers_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class FamilyMembersDelete(DeleteView):
    model = Familymembers
    success_url = reverse_lazy("adminfamilylist")

class FamilyMembersList(TemplateView):
    template_name = "../templates/admin_section/familymembers_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = Familymembers.objects.all()
        print(obj)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)

# class MedicalRecordsAdd(TemplateView):
#     template_name = "../templates/admin_section/medicalrecords_add.html"
#     context = {}
#     form_class = Medicalrecordsform

#     def get(self, request, *args, **kwargs):
#         self.context['form'] = self.form_class
#         return render(request, self.template_name, self.context)

#     def post(self,request,*awrgs,**kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('adminrecordslist')
#         else:
#             return redirect('adminrecordsadd')

# class MedicalRecordsEdit(TemplateView):
#     model = Medicalrecords
#     form_class = Medicalrecordsform
#     template_name = "../templates/admin_section/medicalrecords_edit.html"
#     context = {}

#     def get(self, request, *args, **kwargs):
#         id = kwargs.get('pk')
#         qs = self.model.objects.get(id=id)
#         form = self.form_class(instance=qs)
#         self.context['form'] = form
#         return render(request, self.template_name, self.context)

#     def post(self, request, *args, **kwargs):
#         id = kwargs.get("pk")
#         qs = self.model.objects.get(id=id)
#         form = self.form_class(instance=qs, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('adminrecordslist')
#         else:
#             return render(request, self.template_name, self.context)

# class MedicalRecordsView(TemplateView):
#     model = Medicalrecords
#     template_name = "../templates/admin_section/medicalrecords_view.html"
#     context = {}

#     def get(self, request, *args, **kwargs):
#         id = kwargs.get("pk")
#         qs = self.model.objects.get(id=id)
#         self.context['form'] = qs
#         return render(request, self.template_name, self.context)

# class MedicalRecordsDelete(DeleteView):
#     model = Medicalrecords
#     success_url = reverse_lazy("adminrecordslist")

# class MedicalRecordsList(TemplateView):
#     template_name = "../templates/admin_section/medicalrecords_list.html"
#     context = {}

#     def get(self,request,*awrgs,**kwargs):
#         obj = Medicalrecords.objects.all()
#         print(obj)
#         self.context['items'] = obj
#         return render(request,self.template_name,self.context)

class ServicesAdd(TemplateView):
    template_name = "../templates/admin_section/service_add.html"
    context = {}
    form_class = ServiceForm

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self,request,*awrgs,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminservicelist')
        else:
            return redirect('adminserviceadd')

class ServiceEdit(TemplateView):
    model = Service
    form_class = ServiceForm
    template_name = "../templates/admin_section/service_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminservicelist')
        else:
            return render(request, self.template_name, self.context)

class ServiceView(TemplateView):
    model = Service
    template_name = "../templates/admin_section/service_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class ServiceDelete(DeleteView):
    model = Service
    success_url = reverse_lazy("adminservicelist")

class ServiceList(TemplateView):
    template_name = "../templates/admin_section/service_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = Service.objects.all()
        print(obj)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)

class BlogAdd(TemplateView):
    template_name = "../templates/admin_section/blog_add.html"
    context = {}
    form_class = BlogForm

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self,request,*awrgs,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminbloglist')
        else:
            return redirect('adminblogadd')

class BlogEdit(TemplateView):
    model = Blog
    form_class = BlogForm
    template_name = "../templates/admin_section/blog_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminbloglist')
        else:
            return render(request, self.template_name, self.context)

class BlogView(TemplateView):
    model = Blog
    template_name = "../templates/admin_section/blog_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy("adminbloglist")

class BlogList(TemplateView):
    template_name = "../templates/admin_section/blog_list.html"
    context = {}

    def get(self,request,*awrgs,**kwargs):
        obj = Blog.objects.all()
        print(obj)
        self.context['items'] = obj
        return render(request,self.template_name,self.context)

class DoctorAdd(TemplateView):
    template_name = "../templates/admin_section/doctor_add.html"
    context = {}
    form_class = DoctorForm

    def get(self, request, *args, **kwargs):
        self.context['form'] = self.form_class
        return render(request, self.template_name, self.context)

    def post(self,request,*awrgs,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admindoctorlist')
        else:
            return redirect('adminblogadd')

class DoctorEdit(TemplateView):
    model = Blog
    form_class = BlogForm
    template_name = "../templates/admin_section/blog_edit.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get('pk')
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs)
        self.context['form'] = form
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        form = self.form_class(instance=qs, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminbloglist')
        else:
            return render(request, self.template_name, self.context)

class DoctorView(TemplateView):
    model = Blog
    template_name = "../templates/admin_section/blog_view.html"
    context = {}

    def get(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        self.context['form'] = qs
        return render(request, self.template_name, self.context)

class DoctorDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy("adminbloglist")

# class DoctorList(TemplateView):
#     template_name = "../templates/admin_section/blog_list.html"
#     context = {}

#     def get(self,request,*awrgs,**kwargs):
#         obj = Blog.objects.all()
#         print(obj)
#         self.context['items'] = obj
#         return render(request,self.template_name,self.context)


