#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib
import urllib2
import tools.responseu as rsp

"""
User-Agent : 有些服务器或 Proxy 会通过该值来判断是否是浏览器发出的请求
Content-Type : 在使用 REST 接口时，服务器会检查该值，用来确定 HTTP Body 中的内容该怎样解析。
application/xml ： 在 XML RPC，如 RESTful/SOAP 调用时使用
application/json ： 在 JSON RPC 调用时使用
application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用
在使用服务器提供的 RESTful 或 SOAP 服务时， Content-Type 设置错误会导致服务器拒绝服务
"""
def get(URI, args):
    if args:
        values = {"username":args["username"],"password":args["password"]}
        data = urllib.urlencode(values)
        geturl = URI + "?" + data
    else:
        geturl = URI
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    return response.read()


def post(URI, args):
    if args:
        values = {"username":args["username"],"password":args["password"]}
        data = urllib.urlencode(values)
        geturl = URI + "?" + data
    else:
        geturl = URI
    request = urllib2.Request(geturl)
    response = urllib2.urlopen(request)
    return response.read()


def put(URI, args):
    request = urllib2.Request(URI, 'GET')
    response = urllib2.urlopen(request)
    return response.read()


def delete(URI, args):
    request = urllib2.Request(URI, 'GET')
    response = urllib2.urlopen(request)
    return response.read()


def options(URI, args):
    request = urllib2.Request(URI, 'GET')
    response = urllib2.urlopen(request)
    return response.read()


def head(URI, args):
    request = urllib2.Request(URI, 'GET')
    response = urllib2.urlopen(request)
    return response.read()


def trace(URI, args):
    request = urllib2.Request(URI, 'GET')
    response = urllib2.urlopen(request)
    return response.read()


def connect(URI, args):
    request = urllib2.Request(URI, 'GET')
    response = urllib2.urlopen(request)
    return response.read()
