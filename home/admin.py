from django.contrib import admin
from .models import Department,Purpose,Course,Detail
# Register your models here.
admin.site.register(Department)
admin.site.register(Purpose)
admin.site.register(Course)
admin.site.register(Detail)