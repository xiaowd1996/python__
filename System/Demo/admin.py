#coding:utf-8
from django.contrib import admin
from .models import *
# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ('User_Id','Student_Name','Course_Id','Course_Name','Course_Time','Course_Location','Course_Teacher');
class PersonAdmin(admin.ModelAdmin):
    list_display = ('User_Name', 'User_Password','User_Role');


admin.site.register(Course,CourseAdmin);
admin.site.register(Person,PersonAdmin);