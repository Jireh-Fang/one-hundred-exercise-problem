# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 16:12:46 2019

@author: Administrator
"""

#统计字符'b'出现的次数
str1 = input('输入一段字符：')
count = 0
for i in str1:
    if i == 'b':
        count += 1
print(count)