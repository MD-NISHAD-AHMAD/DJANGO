from django.contrib import admin

# Register your models here.
from student_app.models import *

@admin.register(Student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('student_id','name' ,'age' ,'location' , 'email' ,'course')