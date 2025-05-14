from django.contrib import admin
from .models import *
# Register your models here.

class parentadmin(admin.ModelAdmin):
    list_display = ('father_name','mother_name','father_occuption','mother_occuption','father_email','mother_email','father_mobile','mother_mobile','present_address','permanent_address')
    search_fields = ('father_name','mother_name','father_occuption','mother_occuption','father_email','mother_email','father_mobile','mother_mobile','present_address','permanent_address')
    list_filter = ('father_name','mother_name')
admin.site.register(parents, parentadmin)

class studentadmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','student_id','gender','student_class','blood_group','religion','joining_date','mobile_number','addmission_number','section','student_image','parents','admin_photo')
    search_fields = ('first_name','last_name','student_id','gender','student_class','religion','joining_date','mobile_number','addmission_number','section','student_image','parents')
    list_filter = ('first_name','last_name','gender','student_class','section')
    readonly_fields = ('student_image',)
admin.site.register(student, studentadmin)