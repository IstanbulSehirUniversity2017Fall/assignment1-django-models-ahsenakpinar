from django.contrib import admin
from .models import PhoneBrand,PhoneModel,CategoryModel
# Register your models here.

admin.site.register(PhoneBrand)
admin.site.register(PhoneModel)
admin.site.register(CategoryModel)