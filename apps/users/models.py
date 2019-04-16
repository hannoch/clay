from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
	#昵称
	nickname = models.CharField(max_length=50, blank=True, verbose_name=u'昵称')
	gender_choices = (('male', '男'), ('female', '女'))
	birthday = models.DateField(verbose_name='生日', null=True, blank=True)
	gender = models.CharField(verbose_name='性别', max_length=10, choices=gender_choices, default='female')
	address = models.CharField(verbose_name='地址', max_length=100, default='')
	mobile = models.CharField(verbose_name='手机号', max_length=11, null=True, blank=True)
	image = models.ImageField(upload_to='image/%Y%m', default='image/default.png', max_length=100)
	
	class Meta(AbstractUser.Meta):
		verbose_name = "用户信息"
		verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
	send_choices = (('register', '注册'), ('forget', '找回密码'))
	code = models.CharField(verbose_name='验证码', max_length=20)
	email = models.EmailField(verbose_name='邮箱', max_length=50)
	send_type = models.CharField(choices=send_choices, max_length=10)
	send_time = models.DateTimeField(default=datetime.now)

	class Meta:
		verbose_name = "邮箱验证码"
		verbose_name_plural = verbose_name
