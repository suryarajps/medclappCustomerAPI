from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ServiceDetailView, Userview,RequestView,RequestList,CategoryView,ServiceProviderList,DepartmentView,DoctorView,CustomerLogin,CustomerLogout,SPList,FiltersView

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
    path("details/<int:pk>", ServiceDetailView.as_view()), # not working need to check
    path("request", RequestView.as_view()),
    path("requestlist", RequestList.as_view()),
    path("SPList", SPList.as_view()),
    path('filters/', FiltersView.as_view(), name='Filters')#try


]
urlpatterns = format_suffix_patterns(urlpatterns)
