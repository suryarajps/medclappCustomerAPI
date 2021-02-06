from django.contrib import admin
from Customer.models import Request,Familymembers,Medicalrecords
from Admin_Section.models import Department,Category
from ServiceProvider.models import Doctor,Userprofile,ProfileCompletion


# Register your models here.

# admin.site.register(CustomUser),
admin.site.register(Department),
# admin.site.register(Category),
admin.site.register(Userprofile),
admin.site.register(ProfileCompletion),
admin.site.register(Doctor),
admin.site.register(Request),
admin.site.register(Familymembers),
admin.site.register(Medicalrecords),

