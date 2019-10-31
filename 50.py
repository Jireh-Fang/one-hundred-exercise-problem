# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:02:31 2019

@author: Administrator
"""

#字符串翻转
str1 = 'Crossin的编程教室'
list1 = []
for i in str1:
    list1.append(i)
list2 = list1[::-1]
str2 = ''.join(list2)
print(str2)
