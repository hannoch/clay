from django.conf.urls import url
from . import views

app_name = 'collectMessage' #urls 模块设置命名空间

urlpatterns = [
    url(r'^domain/$', views.domain), #domain.html
    url(r'^resData/$', views.response_data), #data.json
    url(r'^postData/$', views.postData), #get_url
]
