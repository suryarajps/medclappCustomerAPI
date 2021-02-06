from django.db.models import fields
from rest_framework import authentication, exceptions, generics
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as djangologin, logout as djangologout
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from Customer.models import Request
from .serializers import  FiltersSerializers, ProfilecompletioneSerializer, ServiceproviderSerializer,UserCreationSerializer,RequestSerializer,CategorySerializer,DepartmentSerializer,DoctorSerializer,LoginSerializer, UserprofileSerializer
from Admin_Section.models import Category,Department
from ServiceProvider.models import Doctor,CustomUser, ProfileCompletion, Userprofile
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.filters import SearchFilter

# USERS

class Userview(APIView):
    def get(self, request, format=None):
        user = CustomUser.objects.all()
        serializer = UserCreationSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# LOGIN

class CustomerLogin(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        djangologin(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=200)

# LOGOUT

class CustomerLogout(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        djangologout(request)
        return Response(status=204)

#BLOOD REQUEST

class RequestView(APIView):
    def get(self, request, format=None):
        query = Request.objects.all()
        serializer = RequestSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# BLOOD REQUEST LIST.

class RequestList(APIView):

    def get(self, request, format=None):
        query = Request.objects.all()
        serializer = RequestSerializer(query, many=True)
        return Response(serializer.data)


# CATEGORY

class CategoryView(APIView):
    def get(self, request, format=None):
        query = Category.objects.all()
        serializer = CategorySerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# SERVICE PROVIDER LIST (is same as listing category).

class ServiceProviderList(generics.ListAPIView):
    queryset = ProfileCompletion.objects.all()
    serializer_class=ServiceproviderSerializer
    filter_backends = [SearchFilter]
    search_fields = ['fullname', 'category__name','departments__dept_name']

    # def get(self, request, format=None):
    #     query = ProfileCompletion.objects.all()
    #     serializer = ServiceproviderSerializer(query, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request, format=None):
    #     serializer = ServiceproviderSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# SERVICE / Department

class DepartmentView(APIView):
    def get(self, request, format=None):
        query = Department.objects.all()
        serializer = DepartmentSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# DOCTOR

class DoctorView(APIView):
    def get(self, request, format=None):
        query = Doctor.objects.all()
        serializer = DoctorSerializer(query, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class SPList(ObjectMultipleModelAPIView):
    # fields=('phone','email')
    querylist = [
        {'queryset': ProfileCompletion.objects.all(),'serializer_class': ProfilecompletioneSerializer,'label':'Service Provider'},
        {'queryset': Userprofile.objects.all(), 'serializer_class': UserprofileSerializer},
        {'queryset': CustomUser.objects.all(), 'serializer_class': UserCreationSerializer},
    ]

# #try
# class FiltersView(APIView):
#     def get(self,request,*args,**kwargs):
#         filters = {}
#         filters['model_1'] = Userprofile.objects.all()
        
#         filters['model_2'] = ProfileCompletion.objects.all()
        
#         filters['model_3'] = CustomUser.objects.all()
#         print(filters)
#         serializer = FiltersSerializers(filters)
#         return Response (serializer.data, status=status.HTTP_200_OK)


# SERVICE PROVIDER DETAILS

class ServiceDetailView(APIView):
    
    # def get_queryset(self,pk):
    #     print(self.kwargs['pk'])
    #     queryset = ProfileCompletion.objects.get(id=pk)
    #     print(queryset)
    #     queryset =Doctor.objects.filter(organisation=queryset.fullname)
    #     print(queryset)
    #     # qs=Service.objects.filter(category=self.kwargs['pk'])
    #     # print(qs,queryset)
    #     return queryset
    
    # def get(self, request,pk):
    #     query = self.get_queryset(pk)
    #     serializer = DoctorSerializer(query, many=True)
    #     return Response(serializer.data)

    def get_object(self,pk):
        try:
            return ProfileCompletion.objects.get(id=pk)
        except:
            raise Http404

    def get(self, request,pk):
        query = self.get_object(pk)
        serializer = ProfilecompletioneSerializer(query)
        return Response(serializer.data)
    