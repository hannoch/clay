# encoding: utf-8
import django

from index.views import MainView,IndexView

from django.urls import path
app_name = "index"
urlpatterns = [
    # 主界面
    path('index/', IndexView.as_view(), name="index"),
    path('main/', MainView.as_view(), name="index_main"),
    # 首页
]
