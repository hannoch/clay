# encoding: utf-8
import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# 基于类实现需要继承的view
from django.views.generic.base import View


class MainView(View):
	def get(self, request):
		return render(request, "index/main.html")
	
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")

