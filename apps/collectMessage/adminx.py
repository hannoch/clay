#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File : adminx.py
# @Author :hannoch

import xadmin
from .models import Domain

from xadmin import views


# xadmin中这里是继承object，不再是继承admin
class DomainAdmin(object):
	# 显示的列id, NS, IP, Title, Server, Address,GPS,create_time
	list_display = ['NS', 'IP', 'Title', 'Server','Address', 'create_time']
	# 搜索的字段，不要添加时间搜索
	search_fields = ['IP', 'Title', 'Server', ]
	# 过滤
	list_filter = ['IP', 'Title', 'Server', 'create_time']


# 创建xadmin的最基本管理器配置，并与view绑定
class BaseSetting(object):
	# 开启主题功能
	enable_themes = True
	use_bootswatch = True


# 全局修改，固定写法
class GlobalSettings(object):
	# 修改title
	site_title = 'Clay渗透测试后台'
	# 修改footer
	site_footer = 'hannoch'
	# 收起菜单
	menu_style = 'accordion'


# 将title和footer信息进行注册
#xadmin.site.register(views.CommAdminView, GlobalSettings)
# 注册后台
#xadmin.site.unregister(Domain)
#xadmin.site.register(Domain)
xadmin.site.register(Domain, DomainAdmin)


# 将基本配置管理与view绑定
#xadmin.site.register(views.BaseAdminView, BaseSetting)









