#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   clawer_first.py
@Time    :   2020/11/29 22:15:51
@Author  :   HenryWu 
@Version :   1.0
@Contact :   21910069@zju.edu.cn
'''
# Start typing your code from here

# -*- coding:utf-8 -*-
import urllib
import urllib.request
import re

#百度贴吧爬虫类
class BDTB:

    #初始化，传入基地址，是否只看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = '?see_lz='+str(seeLZ)

    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        url = self.baseURL+ self.seeLZ + '&pn=' + str(pageNum)
        response = urllib.request.urlopen(url)
        print(response.read())
        return response

baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
bdtb.getPage(1)
