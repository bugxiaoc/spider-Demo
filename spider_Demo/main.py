#!/usr/bin/python
# -*- coding: UTF-8 -*-

import tools.stringu as str
import tools.requestu as req
import tools.responseu as rsp

def init():
    goble_flag = 0
    while(goble_flag == 0):
        print 'Please Input URI(http://www.baidu.com) Or exit quit :'
        URI = raw_input();
        if (URI == "quit") | (URI =="exit"):
            print 'Tu Dou Bye!'
            goble_flag = 1
            break
        URI = 'https://movie.douban.com/chart'
        rsp_data = req.get(URI, False)
        #电影名称
        xpath = r'//*[@class="pl2"]/a/text()'
        result = rsp.getPath(rsp_data, xpath)
        # 电影评分
        xpath = '//*[@class="star clearfix"]/span[2]/text()'
        result1 = rsp.getPath(rsp_data, xpath)
        # 电影评价人数
        xpath = '//*[@class="star clearfix"]/span[3]/text()'
        result2 = rsp.getPath(rsp_data, xpath)
        str.toString(result,result1,result2)
    print 'Over'

if __name__ == '__main__':
    init();
