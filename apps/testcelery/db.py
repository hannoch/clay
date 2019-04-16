#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File : db.py
# @Author :hannoch

import datetime
import pymysql
from pymysql.cursors import DictCursor

from clay.settings import DATABASES

class Db:
    def __init__(self):
        self.database = DATABASES['default']
        self.database_name = self.database['NAME']
        self.user = self.database['USER']
        self.password = self.database['PASSWORD']
        self.host = self.database['HOST']
        self.port = self.database['PORT']
        self.con = pymysql.connect(self.host, self.user, self.password, self.database_name, self.port, charset='utf8')
        self.con.autocommit(True)

    def close_connect(self):
        self.con.close()

    def get_tasksinfo(self):
        cur = self.con.cursor(DictCursor)
        query_str = "select b.id as id,b.task_id as task_id,b.first as first,b.second as second,b.log_date as logdate,a.status as status,a.result as result,a.traceback as traceback " \
                    "from celery_taskmeta a inner join testcelery_add b on a.task_id=b.task_id;"
        cur.execute(query_str)
        rows = cur.fetchall()
        print(rows)
        cur.close()
        return rows

