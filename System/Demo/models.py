#coding:utf-8
from django.db import models
# Create your models here.
class Course(models.Model):
    User_Id = models.CharField('学号',max_length=1000)#学号
    Student_Name = models.CharField('用户名',max_length=1000)#用户名
    Course_Id = models.CharField('课程序号',max_length=1000)
    Course_Name = models.CharField('课程名',max_length=1000)
    Course_Time = models.CharField('课程时间',max_length=1000)
    Course_Location= models.CharField('课程地点',max_length=1000)
    Course_Teacher = models.CharField('授课教师名',max_length=1000)
    def __unicode__(self):
     return unicode(self.User_Id)
class Person(models.Model):
    User_Name = models.CharField('用户名',max_length=1000);
    User_Password = models.CharField('用户密码',max_length=1000);
    User_Role = models.CharField('用户角色',max_length=1000);