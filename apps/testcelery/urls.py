from django.conf.urls import url
from . import views

app_name = 'testcelery' #urls 模块设置命名空间

from .views import *

urlpatterns = [
    url(r'^index/', index),
    url(r'^add/',add_1),
    url(r'^results/',results),
    ]