from django.conf.urls import url
from . import views

app_name = 'student' #urls 模块设置命名空间

urlpatterns = [
    url(r'^data/$', views.response_data),
    url(r'^allPage/$', views.all_page),  # 前往所有学生的网页
    url(r'^addPage/$', views.add_page),  # 前往新增学生的网页
    url(r'^addStudent/$', views.add_student),  # 添加学生的 dao 操作
    url(r'^search/$', views.search_student),  # 根据 t_name 查找学生的 dao 操作
    url(r'^get/(?P<student_id>[0-9]*)/$', views.search_student_id),  # 根据 id 查找学生的 dao 操作
    url(r'^updateStudent/$', views.update_student),  # 修改学生的 dao 操作
    url(r'^delete/(?P<student_id>[0-9]*)/$', views.delete_student),  # 删除学生的 dao 操作
]
