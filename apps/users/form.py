#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File : form.py
# @Author :hannoch

from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		model = User
		fields = ('username','email')