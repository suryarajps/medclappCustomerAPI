from django.contrib.auth import authenticate
from rest_framework import serializers, exceptions
from Customer.models import Request
from Admin_Section.models import Category,Department
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
    email = serializers.CharField()
    password = serializers .CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                data['user'] = user
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


"""Doctors"""

class DoctorSerializer(serializers.ModelSerializer):
    departments=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Doctor
        fields = ('__all__')
        depth = 2

"""Userprofileserializer"""

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ('coverpicture',)

class ProfilecompletioneSerializer(serializers.ModelSerializer):
    # category=serializers.StringRelatedField(read_only=True)
    # departments=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProfileCompletion
        fields = ('__all__')

"""Serviceprovider"""

class ServiceproviderSerializer(serializers.ModelSerializer):
    # category=serializers.StringRelatedField(read_only=True)
    # coverpicture = UserprofileSerializer(read_only=True)
    # phone=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ProfileCompletion
        fields = ('__all__')
        depth=2

# class ServiceproviderdetailSerializer(serializers.ModelSerializer):


#try
class FiltersSerializers(serializers.Serializer):
    model_1 = Userprofile
    model_2 = ProfileCompletion
    model_3 = CustomUser
    
