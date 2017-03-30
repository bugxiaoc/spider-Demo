#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import urllib2
import requests
import cookielib
from lxml import etree


def getPath(data, pathNode):
    selector = etree.HTML(data)# 转换为xml，用于在接下来识别
    links = selector.xpath(pathNode)
    return links

def createCookie(Self,CookieFileName,url):
    cookie = cookielib.MozillaCookieJar(CookieFileName)
    # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
    handler = urllib2.HTTPCookieProcessor(cookie)
    # 通过handler来构建opener
    opener = urllib2.build_opener(handler)
    response = opener.open(url)
    cookie.save(ignore_discard=True, ignore_expires=True)
    return opener

def readCookie(self,CookieFileName,url):
    # 创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load(CookieFileName, ignore_discard=True, ignore_expires=True)
    # 创建请求的request
    req = urllib2.Request(url)
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    return opener

def Cookie(self,CookieFileName,postdata,geturi,senduri):
    # 声明Cookie对象
    cookie = cookielib.MozillaCookieJar(CookieFileName)
    # 创建Opener对象
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    # 模拟登录，并把cookie保存到变量
    result = opener.open(geturi, postdata)
    # 保存cookie到cookie.txt中
    cookie.save(ignore_discard=True, ignore_expires=True)
    # 请求访问同Cookie网址
    result = opener.open(senduri)
    return result.read()


if __name__ == '__main__':
    cookieFileName = 'conf/cookie.txt'
    request = urllib2.Request("http://www.baidu.com")
    response = urllib2.urlopen(request)
    data = response.read()
    el = getPath(data, '//*[@id="su"]/@value');
    print el

