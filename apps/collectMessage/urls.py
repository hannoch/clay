from django.conf.urls import url
from collectMessage import views

app_name = 'collectMessage' #urls 模块设置命名空间

urlpatterns = [
    url(r'^domain/$', views.domain,name="domain"), #domain.html
    url(r'^resData/$', views.response_data), #data.json
    url(r'^postData/$', views.postData), #get_url
    url(r'^googlehack/$', views.googlehack), #googlehack.html
]
