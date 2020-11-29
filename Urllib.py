#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   Urllib.py
@Time    :   2020/11/29 22:45:48
@Author  :   HenryWu 
@Version :   1.0
@Contact :   21910069@zju.edu.cn
'''
# Start typing your code from here

###主要为了体验Urllib的基本用法
import urllib
import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
print(response.read())