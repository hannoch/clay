from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Domain(models.Model):
	# "insert into domain(id, NS, IP, Title, Server, Address,GPS,create_time)
	NS = models.CharField(max_length=50, null=True,  verbose_name=u'域名')
	IP = models.CharField(verbose_name='ip', null=True, max_length=30, )
	Title = models.CharField(verbose_name='标题', null=True, max_length=50, )
	Server = models.CharField(verbose_name='服务器', null=True, max_length=50, )
	Address = models.CharField(verbose_name='地址', null=True, max_length=100, default='')
	GPS = models.CharField(verbose_name='GPS', max_length=30, null=True, )
	create_time = models.DateTimeField(verbose_name='创建时间', null=True, default=datetime.now)
	
	class Meta:
		verbose_name = "域名解析"
		verbose_name_plural = verbose_name
