#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File : Db.py
# @Author :hannoch
# -*- encoding:utf-8 -*-
import pymysql

class Db():
	def __init__(self, user='root', password='hannoch', dbname='clay', port=3306, host='192.168.52.130'):
		self.host = host
		self.user = user
		self.pwd = password
		self.dbname = dbname
		self.port = port
		if self.connect() is False:
			print(self.dbname + "数据库连接错误！\n")
			return None
		print('数据库连接成功！')
	
	def connect(self):
		try:
			conn = pymysql.connect(host=self.host, user=self.user, password=self.pwd, db=self.dbname, port=self.port,
			                       use_unicode=True, charset="utf8")
			self.conn = conn
			self.cursor = conn.cursor()
		except:
			return False
		return True

	def SelectDomain(self,):
		
		#print("读取人员信息第" + str(start_num) + "到" + str(end_num) + "条")
		# 'select id,book_url from book_info limit 0,10'
		sql = "select * from domain"
		self.cursor.execute(sql)
		self.conn.commit()
		result = self.cursor.fetchall()  # 接收全部的返回结果行.
		if result is None:
			return False
		return result

	# 插入人的信息
	def InsertDomain(self, data):
		#print(data)
		try:
			sql = (
			"insert into domain(id, NS, IP, Title, Server, Address,GPS,create_time) values ('%s','%s','%s','%s','%s','%s','%s','%s')" % (
				data['id'], data['NS'], data['IP'], data['Title'], data['Server'],data['Address'],data['GPS'],data['create_time']))
			print(sql)
			self.cursor.execute(sql)
			self.conn.commit()
		except:
			print('数据库写入出错，操作回滚')
			self.conn.rollback()
			self.conn.commit()
			return
		print('数据库写入成功')
	
	# 插入人的信息
	def InsertPortScan(self, data):
		# print(data)
		try:
			sql = (
					"insert into vulnerabilityScan_portscan(id, IP, port,create_time) values ('%s','%s','%s','%s')" % (
				data['id'],  data['IP'], data['port'],data['create_time']))
			print(sql)
			self.cursor.execute(sql)
			self.conn.commit()
		except:
			print('数据库写入出错，操作回滚')
			self.conn.rollback()
			self.conn.commit()
			return
		print('数据库写入成功')
