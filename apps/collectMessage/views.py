import paramiko
import json
from django.http import HttpResponse
from django.shortcuts import render
import time

from .ssh import Linux
from .tasks import *



#得到数据
def response_data(request):
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
	    "id": "2",
	    "NS": "cs.xmut.edu.cn",
	    "IP": "58.199.200.21",
	    "Title": "计算机与信息工程学院",
	    "Server": "Microsoft-IIS/7.5ASP.NET",
	    "Address": "China Xiamen",
	    "GPS": "24.47/118.0"
	
	  },{
	  "id": "3",
	  "NS": "my.xmut.edu.cn",
	  "IP": "210.34.213.131",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
	
	},{
	  "id": "4",
	  "NS": "www.xmut.edu.cn",
	  "IP": "58.199.200.11",
	  "Title": "厦门理工学院",
	  "Server": "Microsoft-IIS/7.5ASP.NET",
	  "Address": "China Xiamen",
	  "GPS": "24.47/118.0"},{
	  "id": "5",
	  "NS": "mail.xmut.edu.cn",
	  "IP": "210.34.213.13",
	  "Title": "厦门理工学院电子邮件系统",
	  "Server": "nginx/1.10.2",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
	},{
	  "id": "6",
	  "NS": "i.xmut.edu.cn",
	  "IP": "210.34.213.244",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
	}, {
	  "id": "7",
	  "NS": "ids.xmut.edu.cn",
	  "IP": "210.34.213.112",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
	},{
	  "id": "8",
	  "NS": "cis.xmut.edu.cn",
	  "IP": "58.199.200.21",
	  "Title": "厦门理工学院国际教育学院",
	  "Server": "Microsoft-IIS/7.5ASP.NET",
	  "Address": "China Xiamen",
	  "GPS": "24.47/118.0"
	},{
	  "id": "6",
	  "NS": "i.xmut.edu.cn",
	  "IP": "210.34.213.244",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
	}, {
	  "id": "7",
	  "NS": "ids.xmut.edu.cn",
	  "IP": "210.34.213.112",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
	},{
	  "id": "8",
	  "NS": "cis.xmut.edu.cn",
	  "IP": "58.199.200.21",
	  "Title": "厦门理工学院国际教育学院",
	  "Server": "Microsoft-IIS/7.5ASP.NET",
	  "Address": "China Xiamen",
	  "GPS": "24.47/118.0"
	},{
	  "id": "6",
	  "NS": "i.xmut.edu.cn",
	  "IP": "210.34.213.244",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
	}, {
	  "id": "7",
	  "NS": "ids.xmut.edu.cn",
	  "IP": "210.34.213.112",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
	},{
	  "id": "8",
	  "NS": "cis.xmut.edu.cn",
	  "IP": "58.199.200.21",
	  "Title": "厦门理工学院国际教育学院",
	  "Server": "Microsoft-IIS/7.5ASP.NET",
	  "Address": "China Xiamen",
	  "GPS": "24.47/118.0"
	},{
	  "id": "6",
	  "NS": "i.xmut.edu.cn",
	  "IP": "210.34.213.244",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
	}, {
	  "id": "7",
	  "NS": "ids.xmut.edu.cn",
	  "IP": "210.34.213.112",
	  "Title": "None",
	  "Server": "None",
	  "Address": "China Beijing",
	  "GPS": "39.92/116.3"
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

# 1.2.前往domain 页
def domain(request):
	return render(request, 'collectMessage/domain.html')

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




