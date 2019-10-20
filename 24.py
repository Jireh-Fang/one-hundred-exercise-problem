# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:54:20 2019

@author: Administrator
"""

#从控制台输入一段字符，统计字符出现次数
str1 = input('请输入一段字符：')
count = {}
for i in str1:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
print(count)