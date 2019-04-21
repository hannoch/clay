#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @File : config.py
# @Author :hannoch

import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DNSMAPER_DIR = BASE_DIR+'/dnsmaper/'
PORTSCAN_DIR = BASE_DIR+'/portscan/'

PLUGINS_SUPPORT = ['beebeeto', 'pocsuite', 'tangscan']

