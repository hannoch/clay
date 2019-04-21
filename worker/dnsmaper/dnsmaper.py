#!/usr/bin/env python
# -*- coding:utf-8 -*-

import uuid
import requests
import re
import random
import geoip2.database
import os,sys
import time
import optparse
import dns.resolver
import socket
from threading import Thread

from .DBOperator import *


# 初始化数据库

try:
    import queue
except:
    import Queue as queue

class lookup(Thread):

    def __init__(self, in_q, out_q, domain, wildcard = False, resolver_list = []):
        Thread.__init__(self)
        self.in_q = in_q
        self.out_q = out_q
        self.domain = domain
        self.wildcard = wildcard
        self.resolver_list = resolver_list
        self.resolver = dns.resolver.Resolver()
        if len(self.resolver.nameservers):
            self.backup_resolver = self.resolver.nameservers
        else:
            #we must have a resolver,  and this is the default resolver on my system...
            self.backup_resolver = ['127.0.0.1']
        if len(self.resolver_list):
            self.resolver.nameservers = self.resolver_list

    def check(self, host):
        slept = 0
        while True:
            try:
                answer = self.resolver.query(host)
                if answer:
                    return str(answer[0])
                else:
                    return False
            except Exception as e:
                if type(e) == dns.resolver.NXDOMAIN:
                    return False
                elif type(e) == dns.resolver.NoAnswer  or type(e) == dns.resolver.Timeout:
                    if slept == 4:
                        if self.resolver.nameservers == self.backup_resolver:
                            self.resolver.nameservers = self.resolver_list
                        else:
                            self.resolver.nameservers = self.backup_resolver
                    elif slept > 5:
                        self.resolver.nameservers = self.resolver_list
                        return False
                    time.sleep(1)
                    slept += 1
                elif type(e) == IndexError:
                    pass


    def run(self):
        while True:
            sub = self.in_q.get()
            if not sub:
                self.in_q.put(False)
                self.out_q.put(False)
                break
            else:
                test = "%s.%s" % (sub, self.domain)
                addr = self.check(test)
                if addr and addr != self.wildcard:
                    self.out_q.put(test)


def GetUrlInfo(url):
	url = "http://"+url
	try:
		r = requests.get(url,timeout=5)
		r.encoding =  r.apparent_encoding
		title = re.findall("<title>(.*)</title>",r.text)[0].replace('\r','').replace('\n','').replace('\r','').replace(' ','')
		banner = ''
		try:
			banner += r.headers['Server']
		except:
			pass
		try:
			banner += r.headers['X-Powered-By']
		except:
			pass
		return (title,banner)
	except:
		return (u"None"),(u"None")


'''
域名转换IP
'''
def DomainToAddress(domain):
	db = Db()
	try:
		ip=socket.getaddrinfo(domain, None)[0][4][0]
	except:
		print (" URI:%-20s RtnIp Error." % domain)
		return
	GeoDB = geoip2.database.Reader('./worker/dnsmaper/db/GeoLite2-City.mmdb')
	
	
	try:
		res = GeoDB.city(ip)
		address = res.country.name + " " + res.city.name
		latitude = res.location.latitude
		longitude = res.location.longitude
		gps = str(latitude)[0:5]+"/"+str(longitude)[0:5]
		(title,banner) = GetUrlInfo(domain)

		#字段赋值
		title = title[0:13]
		NS = domain
		IP = ip
		Title = title
		Server = banner[0:28]
		Address = address[0:14]
		GPS = gps
		now_time = time.strftime('%Y-%m-%d %H:%M:%S')
		data ={
			'id':uuid.uuid1(),
			'NS':NS,
			'IP':IP,
			'Title':Title,
			'Server':Server,
			'Address':Address,
			"GPS":GPS,
			'create_time':now_time
		}
		
		#输入到数据中
		db.InsertDomain(data)
	except:
		pass
	finally:
		GeoDB.close()

def check_resolvers(file_name):
    ret = []
    resolver = dns.resolver.Resolver()
    res_file = open(file_name).read()
    for server in res_file.split("\n"):
        server = server.strip()
        if server:
            resolver.nameservers = [server]
            try:
                resolver.query("www.google.com")
                ret.append(server)
            except:
                pass
    return ret

def run_target(target, hosts, resolve_list, thread_count):
    threads = []
    wildcard = False
    try:
        resp = dns.resolver.Resolver().query("would-never-be-a-fucking-domain-name-" + str(random.randint(1, 9999)) + "." + target)
        wildcard = str(resp[0])
    except:
        pass
    in_q = queue.Queue()
    out_q = queue.Queue()
    for h in hosts:
        in_q.put(h)
    in_q.put(False)
    step_size = int(len(resolve_list) / thread_count)
    if step_size <= 0:
        step_size = 1
    step = 0
    for i in range(thread_count):
        threads.append(lookup(in_q, out_q, target, wildcard , resolve_list[step:step + step_size]))
        threads[-1].start()
    step += step_size
    if step >= len(resolve_list):
        step = 0

    threads_remaining = thread_count
    while True:
        try:
            d = out_q.get(True, 10)
            if not d:
                threads_remaining -= 1
            else:
                DomainToAddress(d)

        except queue.Empty:
            pass
        if threads_remaining <= 0:
            break

'''
	域传送漏洞检测,适用Linux环境
'''
def dns_zone_transfer_check(domain):
	cmd_res = os.popen('nslookup -type=ns ' + domain).read()
	dns_servers = re.findall('nameserver = ([\w\.]+)', cmd_res)
	for server in dns_servers:
		if len(server) < 5: server += domain
		cmd_res = os.popen('dig @%s axfr %s' % (server, domain)).read()
		if cmd_res.find('Transfer failed.') < 0 and cmd_res.find('connection timed out') < 0 and cmd_res.find('XFR size') > 0 :
			print ('[!]Vulnerable DNS Zone Transfer Found: %s' % server)
			print (cmd_res)
		else:
			print ('[!]DNS Zone Transfer UnVulnerable.')



'''
if __name__ == '__main__':
    parser = optparse.OptionParser("Usage: %prog [options] target")
    parser.add_option("-c", "--thread_count", dest = "thread_count",
              default = 17, type = "int",
              help = "[optional]number of lookup theads,default=17")
    parser.add_option("-s", "--subs", dest = "subs", default = "./db/subs.db",
              type = "string", help = "(optional)list of subdomains,  default='./db/subs.db'")
    parser.add_option("-r", "--resolvers", dest = "resolvers", default = "./db/resolvers.db",
              type = "string", help = "(optional)list of DNS resolvers,default='./db/resolvers.db'")
    (options, args) = parser.parse_args()
    LogList = []
    LogFile = []
    if len(args) < 1:
        print ("[-]Target Plz! Use -h for help.")
        exit(1)
    targets = args
    for target in targets:
        target = target.strip()
    dns_zone_transfer_check(target)
    hosts = open(options.subs).read().split("\n")
    print ('\n[!]Check DNS Resolvers..')
    resolve_list = check_resolvers(options.resolvers)
    threads = []
    print(hosts)
    run_target(target, hosts, resolve_list, options.thread_count)
    print ("[*]All Done.")
'''