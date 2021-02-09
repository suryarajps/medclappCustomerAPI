from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogView, FamilyView, ServiceDetailView, Userview,RequestView,RequestList,CategoryView,ServiceProviderList,DepartmentView,DoctorView,CustomerLogin,CustomerLogout,CustomerView

urlpatterns = [
    path("userview", Userview.as_view()), #signup and list
#     path("profile", ProfileCompletion.as_view()),
#     path("profile/<int:pk>", Customerprofiledetails.as_view()),
    path("login", CustomerLogin.as_view()),
    path("logout", CustomerLogout.as_view()),
    path("category", CategoryView.as_view()),
    path("department", DepartmentView.as_view()),
    path("doctor", DoctorView.as_view()),
    path("list", ServiceProviderList.as_view()), 
    path("details/<int:pk>", ServiceDetailView.as_view()),
    path("request", RequestView.as_view()),
    path("requestlist", RequestList.as_view()),
    path("customer",CustomerView.as_view()),
    path("family",FamilyView.as_view()),
    path("blog",BlogView.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)
