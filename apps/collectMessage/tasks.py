
from __future__ import absolute_import
from celery import shared_task

from bs4 import BeautifulSoup

from worker.dnsmaper.dnsmaper import *
import requests
import json

#信息收集
class Whoissearch(object):
    def __init__(self, url):
        # 初始化url
        self.result = {}
        self.IPList = ""
        self.DomainInfo = ""
        self.BeianInfo = ""
        self.WhoisInfo = ""
        self.urlIndex = "http://site.ip138.com/{}/".format(url)
        self.urlDomain = "http://site.ip138.com/{}/domain.htm".format(url)
        self.urlBeian = "http://site.ip138.com/{}/beian.htm".format(url)
        self.urlWhois = "http://site.ip138.com/{}/whois.htm".format(url)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    
    # 解析ＩＰ
    def GetIP(self):
        temp = ""
        responseIndex = requests.get(self.urlIndex, headers=self.headers)
        SoupIndex = BeautifulSoup(responseIndex.content, 'html.parser')
        for x in SoupIndex.find_all('p'):
            link = x.get_text()
            #self.IPList = link + self.IPList
            temp = link + temp
        self.IPList = temp
 
    # 域名信息
    def GetDomain(self):
        temp = ""
        responseDomain = requests.get(self.urlDomain, headers=self.headers)
        SoupDomain = BeautifulSoup(responseDomain.content, 'html.parser')
        for x in SoupDomain.find_all('p'):
            link = x.get_text()
            temp = link + temp
        self.DomainInfo = temp

    # 备案信息
    def GetBeian(self):
        temp = ""
        responseBeian = requests.get(self.urlBeian, headers=self.headers)
        SoupBeian = BeautifulSoup(responseBeian.content, 'html.parser')
        for x in SoupBeian.find_all('p'):
            link = x.get_text()
            temp = link + temp
            #self.BeianInfo = link + self.BeianInfo
        self.BeianInfo = temp
        print(self.BeianInfo)
    
    # print("*" * 10)
    # whois信息
    def GetWhois(self):
        temp = ""
        responseWhois = requests.get(self.urlWhois, headers=self.headers)
        SoupWhois = BeautifulSoup(responseWhois.content, 'html.parser')
        for x in SoupWhois.find_all('p'):
            link = x.get_text()
            #self.WhoisInfo = link + self.WhoisInfo
            temp = link + temp
        self.WhoisInfo = temp
        # print(link)
    
    # print("*" * 10)
    
    def run(self):
        self.GetIP()
        self.GetDomain()
        self.GetBeian()
        self.GetWhois()
        #print(self.IPList.encode("utf-8"))
        data = {
            'IPList': self.IPList,
            'DomainInfo': self.DomainInfo,
            'BeianInfo': self.BeianInfo,
            'WhoisInfo': self.WhoisInfo
        }
        print(data)
        return data





@shared_task(track_started=True)
def dnsmaper(url):
    
    dns_zone_transfer_check(url)
    hosts = "./db/subs.db".split("\n")
    print('\n[!]Check DNS Resolvers..')
    resolve_list = check_resolvers("./db/resolvers.db")
    threads = []
    run_target(url, hosts, resolve_list, 17)
    print("[*]All Done.")
#信息收集
@shared_task(track_started=True)
def whoisinfo(url):
    obj = Whoissearch(url)
    Jsondata = obj.run()
    
    return Jsondata


