from django.contrib import admin

from ServiceProvider.models import CustomUser
from Admin_Section.models import Category
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Category)