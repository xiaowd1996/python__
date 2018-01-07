# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


from .models import *


# 首界面
def IndexRender(request):
    return render(request, 'Index.html');
# 教师登录模版
def TeacherLoginRender(request):
    return render(request, 'teacherLogin.html')
def StudentLoginRender(request):
    return render(request,'teacherLogin.html')
#学生查看课表模版
def StudentViewCourse(request):
    course = Course.objects.all();
    return render(render, 'show2.html', {"course": course})
# 课程表录入模版
def addCourseRender(request):
    return render(request,'AddCourse.html')
#查看课程信息
def showCourseRender(request):
    course = Course.objects.all();
    print course;
    return render(request,'show.html',{"course":course})
def updateCoureRender(request,studentId,courseId):
    print courseId,studentId;
    course = Course.objects.filter( User_Id=studentId,Course_Id=courseId);
    return render(request,'update.html',{"course":course})


# 教师登录处理
def Login(request):
    if (request.method == "POST"):
        UserAccount = request.POST.get('name');  # 获取用户名
        USerPasswoed = request.POST.get('password');  # 获取用户密码
        userInfo = Person.objects.filter(User_Name=UserAccount, User_Password=USerPasswoed);  # 向数据库查询是否有该条记录
        if(userInfo):
            if (userInfo[0].User_Role == '1'):#管理员登录
             return render(request, "Admin.html");  # 返回用户管理界面
            elif(userInfo[0].User_Role == '0'):#普通用户登录
             course = Course.objects.filter(User_Id=UserAccount); #为学号
             return render(request, 'SearchReault.html', {"course": course})

        else:
            return HttpResponse("帐号或密码错误， 请重试！");  # 如果帐号或密码错误
    else:
        return render(request, "Admin.html");  # 返回用户管理界面

#课程表添加
def AddCourse(request):
    if (request.method == "POST"):
        studentId = request.POST.get("studentId");  # 获取用户名
        studentName = request.POST.get("studentName");  # 获取用户名
        courseId = request.POST.get("courseId");  # 获取用户名
        courseName = request.POST.get("courseName");  # 获取用户名
        courseTime = request.POST.get("courseTime");  # 获取用户名
        courseLocation = request.POST.get("courseLocation");  # 获取用户名
        Teacher= request.POST.get("Teacher");  # 获取用户名

        #插入数据
        flag = Course.objects.get_or_create(User_Id = studentId,
                                            Student_Name = studentName,
                                            Course_Id = courseId,
                                            Course_Name =courseName,
                                            Course_Time = courseTime,
                                            Course_Location = courseLocation,
                                            Course_Teacher = Teacher
                                            )
        if(flag):
            return HttpResponse("添加成功");

#更新课程
def UpdateCourse(request):
    studentId = request.POST.get("studentId");  # 获取用户名
    studentName = request.POST.get("studentName");  # 获取用户名
    courseId = request.POST.get("courseId");  # 获取用户名
    courseName = request.POST.get("courseName");  # 获取用户名
    courseTime = request.POST.get("courseTime");  # 获取用户名
    courseLocation = request.POST.get("courseLocation");  # 获取用户名
    Teacher = request.POST.get("Teacher");  # 获取用户名
    course = Course.objects.filter(Course_Id=courseId,User_Id=studentId).update(User_Id = studentId,
                                            Student_Name = studentName,
                                            Course_Id = courseId,
                                            Course_Name =courseName,
                                            Course_Time = courseTime,
                                            Course_Location = courseLocation,
                                            Course_Teacher = Teacher);
    if(course):
        return HttpResponse("更新成功");
#删除信息
def Delete(request,studentId,courseId):
   flag =  Course.objects.filter(Course_Id=courseId, User_Id=studentId).delete();
   return HttpResponse("删除成功,<a href ='/show/' >返回</a>");
def Search(request):
    if (request.method == "POST"):
        studentId = request.POST.get('studentId');  # 获取用户名
        course = Course.objects.filter(User_Id=studentId);
        return render(request, 'SearchReault.html', {"course": course})

#添加用户模版
def addUserRender(request):
    return render(request,'Adduser.html');
#添加用户
def AddUser(request):
    if (request.method == "POST"):
        UserAccount = request.POST.get('studentId');  # 获取用户名
        USerPasswoed = request.POST.get('studentpassword');  # 获取用户密码
        Person.objects.get_or_create(User_Name = UserAccount,User_Password = USerPasswoed,User_Role = '0')
        return HttpResponse("添加成功");