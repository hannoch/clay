#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File : celery.py.py
# @Author :hannoch

import os
from celery import Celery

# 把置默认的django settings模块配置给celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clay.settings')

app = Celery('clay')

# 这里使用字符串以使celery的worker不用为子进程序列化配置对象。
# 命名空间 namespace='CELERY'定义所有与celery相关的配置的键名要以'CELERY_'为前缀。
app.config_from_object('django.conf:settings', namespace='CELERY')

# 从所有django app configs中加载task模块，
# 如果你把所有的task都定义在单独的tasks.py模块中，
# 加上这句话celery会自动发现这些模块中的task，实际上这句话可以省略。
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
