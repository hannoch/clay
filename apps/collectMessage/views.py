# encoding: utf-8

from django.db.models import Q
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.core import serializers
import time
import paramiko
import json

from .tasks import *
from collectMessage.models import Domain


def response_data(request):
	if request.method == 'GET':
		#all_domain = Domain.objects.all()
		# 使用ORM
		# all()返回的是QuerySet 数据类型；values()返回的是ValuesQuerySet 数据类型
		all_domain = Domain.objects.values('id', 'IP', 'NS', 'Title','Server','Address','GPS','create_time')
		return JsonResponse(list(all_domain), safe=False)
		

#得到数据
def response_data2(request):
	if request.method == 'GET':
		
		data = [{
	  "id": "1",
	  "NS": "search.xmut.edu.cn",
	  "IP": "58.199.200.12",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Xiamen",
	  "GPS": "24.47/118.0"
	
	},{
	  "id": "8",
	  "NS": "cis.xmut.edu.cn",
	  "IP": "58.199.200.21",
	  "Title": "厦门理工学院国际教育学院",
	  "Server": "Microsoft-IIS/7.5ASP.NET",
	  "Address": "China Xiamen",
	  "GPS": "24.47/118.0"
	}]
		
		return HttpResponse(json.dumps(data), content_type="application/json")

# 前往domain 页
def domain(request):
	return render(request, 'collectMessage/domain.html')

# 前往domain 页
def googlehack(request):
	return render(request, 'collectMessage/googleHack.html')

# 前往baseinfo 页
def baseinfo(request):
	if request.method == "GET":
		return render(request, 'collectMessage/baseInfo.html')
	
	if request.method == "POST":
		'''
		linux	通过表单提交之后,变成了POST请求
		'''
		# 获取POST里面的信息
		url = request.POST["url"]
		#实例化Ｃelery
		resultID = whoisinfo.delay(url)
		datadict = resultID.get()
		context = {}
		context['data'] = datadict
		print(datadict)
		return render(request, 'collectMessage/baseInfo.html',context)

"""
从domain.html input 中得到数据
"""
def postData(request):
	'''
	    request就是HttpRequest对象
	    HttpResponse常用的扩展对象
	        render:页面渲染,可将参数以字典的形式传递给页面 也可以通过locals()将参数传递过去,没有进行页面跳转,url没有改变
	        redirect:页面跳转,url发生改变
	    :param request:
	    :return:
	'''
	
	if request.method == "POST":
		'''
		linux	通过表单提交之后,变成了POST请求
		'''
		# 获取POST里面的信息
		ret = request.POST
		print(ret['url'])

		#实例化Ｃelery
		result = dnsmaper.delay(ret['url'])
		print('task done: {0}'.format(result.get()))
		'''
		输出  POST信息 <QueryDict: {'csrfmiddlewaretoken': ['oeKNHGKKm9Ip6B4Y2bfZM16lD2ECoTylPzX7rKzEUO5baf5Dfw4uB2zz5zz61fL9'], 'username': ['Jason'], 'pwd': ['123'], 'gender': ['1']}>

		也是一个字典对象,可以通过句点获取表单提交过来的数据
		'''

		return render(request, 'collectMessage/domain.html')




