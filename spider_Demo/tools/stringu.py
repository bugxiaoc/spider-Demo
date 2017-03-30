#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

"""
   String Util
"""
def checkURI(str):
    if re.search('',str,re.S):
        return 1
    else:
        return 0

def delete_space(obj):
    while '' in obj:
        obj.remove('')
    return obj
def fromat_list(obj):
    temp = []
    for x in obj:
        temp.append(x.strip().replace("\n", "").replace(" ", ""))
    return temp

def toString(result,result1):
    ls1 = delete_space(fromat_list(result))
    ls2 = delete_space(fromat_list(result1))
    for i in range(0,len(ls1)):
        print ls1[i],ls2[i]

def toString(result,result1,result2):
    ls1 = delete_space(fromat_list(result))
    ls2 = delete_space(fromat_list(result1))
    ls3 = delete_space(fromat_list(result2))
    for i in range(0,len(ls1)):
        print ls1[i],ls2[i],ls3[i]