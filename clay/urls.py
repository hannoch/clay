"""clay URL Configuration

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
#from django.contrib import admin
import django
from django.contrib import admin
from django.urls import path, include, re_path
# 导入x admin，替换admin
from django.views.static import serve

import users
import xadmin
from django.views.generic import TemplateView
# from users.views import user_login
from clay.settings import MEDIA_ROOT

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView


urlpatterns = [
    path('admin/', xadmin.site.urls),
    # 别忘记在顶部引入 views 模块
    path('collectMessage/', include('collectMessage.urls')),
    path('vulnerabilityScan/', include('vulnerabilityScan.urls')),
    path('index/', include('index.urls',namespace="index")),
    # TemplateView.as_view会将template转换为view
    #path('', TemplateView.as_view(template_name="login.html"), name="index"),
    # 基于类方法实现登录,这里是调用它的方法
    path('', LoginView.as_view(), name="login"),
    # 退出功能url
    path('logout/', LogoutView.as_view(), name="logout"),
    
    # 注册url
    path("register/", RegisterView.as_view(), name="register"),
    
    # 验证码url
    re_path(r"^captcha/", include('captcha.urls')),
    #path('get_valid_img.png/', GetAlidImgView.as_view,name = "get_valid_img.png"),
    # 激活用户url
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name="user_active"),
    
    # 忘记密码
    path('forget/', ForgetPwdView.as_view(), name="forget_pwd"),
    
    # 重置密码urlc ：用来接收来自邮箱的重置链接
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name="reset_pwd"),
    
    # 修改密码url; 用于passwordreset页面提交表单
    path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),
    
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    # user app的url配置
    path("users/", include('users.urls', namespace="users")),
    
    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),
]
