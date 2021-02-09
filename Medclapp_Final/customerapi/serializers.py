from django.contrib.auth import authenticate
from django.db.models import fields
from rest_framework import response, serializers, exceptions
from Customer.models import CustomerProfile, Familymembers, Request
from Admin_Section.models import Blog, Category,Department
from ServiceProvider.models import Doctor,CustomUser, ProfileCompletion, Userprofile


"""User creation"""

class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # fields = ['password','phone']
        fields =('phone','email','password')

    def create(self, validated_data):
        user = CustomUser(
            email=validated_data['email'],
            phone=validated_data['phone']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

"""Login"""

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers .CharField()
    
    def validate(self, data):
        phone = data.get('phone')
        password = data.get('password')
        reg=False
        print(phone,",",password)
        obj = CustomUser.objects.get(phone=phone)
        if phone and password:
            user = authenticate(email=obj.email, password=password)
            if user:
                data['user'] = user
                # msg = 'registered user'
                # raise response({msg})
                # # if user.is_authenticated:
                # obj1=CustomerProfile.objects.all()
                # if obj1.exists():
                #     for datas in obj1:
                #         print(datas.user)
                #         if user.email==datas.user:
                #             print(user.email)
                #             msg = 'registered user'
                #             raise response({msg})
            else:
                msg = 'login failed'
                raise exceptions.ValidationError(msg)
        else:
            msg = 'provide credientials'
            raise exceptions.ValidationError(msg)
        return data


"""BloodRequest"""

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ('__all__')

"""Category"""

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


"""Service, Department"""

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('__all__')

class ProfilecompletioneSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProfileCompletion
        fields = ('id','fullname','address','user','location','coverpicture','photo','bed_numbers','category','departments')
        category=CategorySerializer(read_only=True)
        departments=DepartmentSerializer(read_only=True)


"""Doctors"""

class DoctorSerializer(serializers.ModelSerializer):
    departments=serializers.StringRelatedField(read_only=True)
    # organisation=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Doctor
        fields = ('__all__')
        depth = 2

"""Userprofileserializer"""

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ('coverpicture',)



"""Serviceprovider"""

class ServiceproviderSerializer(serializers.ModelSerializer):
    # category=serializers.StringRelatedField(read_only=True)
    # coverpicture = UserprofileSerializer(read_only=True)
    # phone=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProfileCompletion
        fields =('id','fullname','address','user','location','coverpicture','photo','category')
        depth=2

"""Customer creation"""

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model:CustomerProfile
        fields = ('fullname','bloodgroup','gender','dOB','height','weight','address','profilepicture')


"""Family """

class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model:Familymembers
        fields = ('fullname','gender','dOB','relationship','phone',)


"""Blog"""

class BlogSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=Blog
        fields="__all__"