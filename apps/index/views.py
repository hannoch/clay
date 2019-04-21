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

class NewsListView(View):
    def get(self, request):
        return render(request, "index/newsList.html")

class NewsAddView(View):
    def get(self, request):
        return render(request, "index/newsAdd.html")

class LinksListView(View):
    def get(self, request):
        return render(request, "index/linksList.html")

class LinksAddView(View):
    def get(self, request):
        return render(request, "index/linksAdd.html")

class SystemParameterView(View):
    def get(self, request):
        return render(request, "index/systemParameter.html")
    
class MessageView(View):
    def get(self, request):
        return render(request, "index/message.html")

class MessageReplyView(View):
    def get(self, request):
        return render(request, "index/messageReply.html")

class ErrorPageView(View):
    def get(self, request):
        return render(request, "index/404.html")
