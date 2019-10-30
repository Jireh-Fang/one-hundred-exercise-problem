# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 19:25:22 2019

@author: Administrator
"""
a = True
while a:
    str1 = input('请输入一串字符： ')
    if str1.isdigit():
        print('该字符串是数字')
        a = False
    else:
        print('该字符串不是全数字')