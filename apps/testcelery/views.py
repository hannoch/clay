#__*__coding:utf-8__*__
from django.shortcuts import render

# Create your views here.

from clay import settings    # 获取 settings.py 里边配置的信息
import os
import json

from django.shortcuts import render_to_response

from .tasks import add
from .models import Add
from .db import Db
import datetime


def index(request):
    return  render_to_response('testcelery/index.html')

def add_1(request):
    first = int(request.GET.get('first'))
    second = int(request.GET.get('second'))
    result = add.delay(first,second)
    dd = Add(task_id=result.id,first=first,second=second,log_date=datetime.datetime.now())
    dd.save()
    return render_to_response('testcelery/index.html')

# 任务结果
def results(request):
    #查询所有的任务信息
    rows = Add.objects.all()
    #db = Db()
    #rows = db.get_tasksinfo()
    print(rows)
    return render_to_response('testcelery/result.html',{'rows':rows})
