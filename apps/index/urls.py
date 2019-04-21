# encoding: utf-8
import django

from index.views import *

from django.urls import path
app_name = "index"
urlpatterns = [
    # 主界面
    path('index/', IndexView.as_view(), name="index"),
    path('main/', MainView.as_view(), name="index_main"),

    path('newslist/', NewsListView.as_view(), name="newslist"),
    path('newsadd/', NewsAddView.as_view(), name="newsadd"),
    
    path('linkslist/', LinksListView.as_view(), name="linkslist"),
    path('linksadd/', LinksAddView.as_view(), name="linksadd"),
    
    path('systemparameter/', SystemParameterView.as_view(), name="systemparameter"),
    
    path('messagereply/', MessageReplyView.as_view(), name="messagereply"),
    path('message/', MessageView.as_view(), name="message"),
    path('error/', ErrorPageView.as_view(), name="error"),
]
