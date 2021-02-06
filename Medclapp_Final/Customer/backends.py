from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

from ServiceProvider.models import CustomUser

class CustomerBackend(ModelBackend):

    def Customauthenticate(self, request, **kwargs):
        phone = kwargs['phone']
        password = kwargs['password']
        try:
            customer = CustomUser.objects.get(phone=phone)
            if customer.user.check_password(password) is True:
                return customer.user
        except CustomUser.DoesNotExist:
            pass