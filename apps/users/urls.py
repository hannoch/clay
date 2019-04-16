#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File : urls.py
# @Author :hannoch

from django.conf.urls import url
from . import views

app_name = 'users' #urls 模块设置命名空间
urlpatterns = [
	url(r'register', views.register, name='register'),
]