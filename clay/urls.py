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
from django.urls import path,include
from django.views.generic import TemplateView

import xadmin

from users import views
from collectMessage import views
from testcelery import views

urlpatterns = [
    path('admin/', xadmin.site.urls),
    path('users/', include('users.urls')),
    # 将 auth 应用中的 urls 模块包含进来
    path('users/', include('django.contrib.auth.urls')),
    # 别忘记在顶部引入 views 模块
    path('collectMessage/', include('collectMessage.urls')),
    #path('', views.index, name='index'),
    path('testcelery/', include('testcelery.urls')),
    #path('', views.index, name='index'),
]
