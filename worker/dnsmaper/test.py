#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File : test.py
# @Author :hannoch
# -*- coding: utf-8 -*-
import os
import pymysql
import time
from .DBOperator import *

def test():
	db = Db()
	list = db.SelectDomain()
	for item in list:
		print(item)
	return list

