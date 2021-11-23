"""myWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.test),
    path('', views.index),
    path('notice/', views.notice),
    #path('board/<int:boardId>', views.board),
    path('language/<languageId>', views.language),
    re_path(r'reg1/(.)/', views.reg1),
    re_path(r'reg2/(..)/', views.reg2),
    re_path(r'reg3/(.{5})/', views.reg3),
    re_path(r'reg4/(.{3}|.{5})/', views.reg4),
    re_path(r'reg5/(.{3,5})/', views.reg5),
    re_path(r'reg6/(.+)/', views.reg6),
    re_path(r'reg7/(.*)/', views.reg7),
    re_path(r'reg8/([0-9])/', views.reg8),
    re_path(r'reg9/([0-9]{3})/', views.reg9),
    re_path(r'reg10/([0-9][0-9][0-9])/', views.reg10),
    re_path(r'reg11/(20[0-1][0-9]|202[0-1])/', views.reg11),
    re_path(r'reg12/([a-zA-Z0-9ㄱ-힣]+)/', views.reg12),
    re_path(r'reg13/([a-zA-Z0-9]+@[a-z]+.[a-z]+)/', views.reg13),
    re_path(r'reg14/(01[0-2]-[0-9]{4}-[0-9]{4})/', views.reg14),
    re_path(r'reg15/(\d+)',views.reg15),
    re_path(r'reg16/(\w+)',views.reg16),
    re_path(r'email/(\w+[@]\w+[.]\w{3}|\w+[@]\w+[.]\w+[.]\w+)', views.email),
    re_path(r'lang/(ko|en|jp)/', views.lang),
    path('board/', include('board.urls')),
    path('chart/', include('chart.urls')),
    path('temp1/', views.temp1),
    path('temp2/', views.temp2),
    path('temp3/', views.temp3),
    path('quiz01/', views.quiz01),
    path('quiz02/', views.quiz02),
    path('quiz03/', views.quiz03),
    path('image/', views.image),
]
