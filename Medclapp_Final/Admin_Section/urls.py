from django.contrib import admin
from django.urls import path,include
from Admin_Section.views import index,ServiceProviderList,ServiceProviderService,CustomerList,DoctorList,CustomerAdd,CustomerEdit,CustomerView,CustomerDetail,CustomerDelete,ProviderList,Requestcreate,Requestedit,Requestlist,Requestdelete,Requestview
from Admin_Section.views import BloodEmergency,BloodModerate,BloodNormal,BloodHour,ProviderList,ProviderEdit,ProviderDelete,ProviderAdd,ProviderView,CategoryList,CategoryView,CategoryAdd,CategoryEdit,CategoryDelete
from Admin_Section.views import DepartmentAdd,DepartmentDelete,DepartmentEdit,DepartmentList,DepartmentView,AdvertisementAdd,AdvertisementDelete,AdvertisementEdit,AdvertisementList,AdvertisementView,FamilyMembersAdd,FamilyMembersDelete,FamilyMembersEdit,FamilyMembersList,FamilyMembersView
# MedicalRecordsAdd,MedicalRecordsDelete,MedicalRecordsEdit,MedicalRecordsList,MedicalRecordsView,
from Admin_Section.views import ServicesAdd,ServiceEdit,ServiceDelete,ServiceList,ServiceView,BlogAdd,BlogDelete,BlogEdit,BlogView,BlogList
from Customer.views import loginn as custlogin
from ServiceProvider.views import loginpage

urlpatterns = [
    path('',index,name="adminindex"),
    path('custom',custlogin.as_view(),name="custompage"),
    path("login",loginpage.as_view(),name="login"),
    path('servicelist',ServiceProviderList.as_view(),name="adminservice"),
    path('service/<int:pk>',ServiceProviderService.as_view(),name="service"),
    path('customerdetail',CustomerDetail.as_view(),name="admincustomerdetail"),
    path('customerlist',CustomerList.as_view(),name="admincustomerlist"),
    path('doctorlist',DoctorList.as_view(),name="admindoctorlist"),
    path('customeradd',CustomerAdd.as_view(),name ="admincustomeradd"),
    path('customeredit/<int:pk>',CustomerEdit.as_view(),name ="admincustomeredit"),
    path('customerview/<int:pk>',CustomerView.as_view(),name ="admincustomerview"),
    path('customerdelete/<int:pk>',CustomerDelete.as_view(),name ="admincustomerdelete"),
    path('create',Requestcreate.as_view(),name ="create"),
    path('edit/<int:pk>',Requestedit.as_view(),name ="edit"),
    path('list',Requestlist.as_view(),name ="list"),
    path('delete/<int:pk>',Requestdelete.as_view(),name ="delete"),
    path('view/<int:pk>',Requestview.as_view(),name ="view"), 
    path('emergency',BloodEmergency.as_view(),name="emergency"),
    path('moderate',BloodModerate.as_view(),name="moderate"),
    path('normal',BloodNormal.as_view(),name="normal"),
    path('24hour',BloodHour.as_view(),name="24hour"),
    path('provideradd',ProviderAdd.as_view(),name="provideradd"),
    path('provideredit/<int:pk>',ProviderEdit.as_view(),name ="provideredit"),
    path('providerview/<int:pk>',ProviderView.as_view(),name ="providerview"),
    path('providerdelete/<int:pk>',ProviderDelete.as_view(),name ="providerdelete"),
    path('providerlist',ProviderList.as_view(),name="providerlist"),
    path('categoryadd',CategoryAdd.as_view(),name ="admincategoryadd"),
    path('categoryedit/<int:pk>',CategoryEdit.as_view(),name ="admincategoryedit"),
    path('categoryview/<int:pk>',CategoryView.as_view(),name ="admincategoryview"),
    path('categorydelete/<int:pk>',CategoryDelete.as_view(),name ="admincategorydelete"),
    path('categorylist',CategoryList.as_view(),name="admincategorylist"),
    path('departmentadd',DepartmentAdd.as_view(),name ="admindepartmentadd"),
    path('departmentedit/<int:pk>',DepartmentEdit.as_view(),name ="admindepartmentedit"),
    path('departmentview/<int:pk>',DepartmentView.as_view(),name ="admindepartmentview"),
    path('departmentdelete/<int:pk>',DepartmentDelete.as_view(),name ="admindepartmentdelete"),
    path('departmentlist',DepartmentList.as_view(),name="admindepartmentlist"), 
    path('advertisementadd',AdvertisementAdd.as_view(),name ="adminadvertisementadd"),
    path('advertisementedit/<int:pk>',AdvertisementEdit.as_view(),name ="adminadvertisementedit"),
    path('advertisementview/<int:pk>',AdvertisementView.as_view(),name ="adminadvertisementview"),
    path('advertisementdelete/<int:pk>',AdvertisementDelete.as_view(),name ="adminadvertisementdelete"),
    path('advertisementlist',AdvertisementList.as_view(),name="adminadvertisementlist"),
    path('familymembersadd',FamilyMembersAdd.as_view(),name='adminfamilyadd'),
    path('familymembersedit/<int:pk>',FamilyMembersEdit.as_view(),name='adminfamilyedit'),
    path('familymembersview/<int:pk>',FamilyMembersView.as_view(),name='adminfamilyview'),
    path('familymembersdelete/<int:pk>',FamilyMembersDelete.as_view(),name='adminfamilydelete'),
    path('familymemberslist',FamilyMembersList.as_view(),name='adminfamilylist'),
    path('serviceadd',ServicesAdd.as_view(),name='adminserviceadd'),
    path('serviceedit/<int:pk>',ServiceEdit.as_view(),name='adminserviceedit'),
    path('serviceview/<int:pk>',ServiceView.as_view(),name='adminserviceview'),
    path('servicedelete/<int:pk>',ServiceDelete.as_view(),name='adminservicedelete'),
    path('servicelist',ServiceList.as_view(),name='adminservicelist'),
    path('blogadd',BlogAdd.as_view(),name='adminblogadd'),
    path('blogedit/<int:pk>',BlogEdit.as_view(),name='adminblogedit'),
    path('blogview/<int:pk>',BlogView.as_view(),name='adminblogview'),
    path('blogdelete/<int:pk>',BlogDelete.as_view(),name='adminblogdelete'),
    path('bloglist',BlogList.as_view(),name='adminbloglist'),       
]