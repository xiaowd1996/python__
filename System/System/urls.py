# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from Demo import  views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexRender),
    url(r'^teacher/$', views.TeacherLoginRender),
    url(r'^student/$', views.StudentLoginRender),
    url(r'^welcome/$', views.Login),
    url(r'^add/$', views.addCourseRender),
    url(r'^addcourse/$', views.AddCourse),
    url(r'^show/$', views.showCourseRender),
    url(r'^update/ (.+) (.+)/$', views.updateCoureRender,name='update'),
    url(r'^delete/ (.+) (.+)/$', views.Delete, name='delete'),
    url(r'^updatecourse/$', views.UpdateCourse),
    url(r'^search/$', views.Search),
    url(r'^adduser/$', views.addUserRender),
    url(r'^adduser2/$', views.AddUser),



]
