# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:04:31 2019

@author: Administrator
"""

#信息加密
num = input('请输出四位数字：')
list1 = []
for i in num:
    res = (int(i)+5)%10
    list1.append(res)
list1[0],list1[1],list1[2],list1[3]=list1[3],list1[2],list1[1],list1[0] #列表交换元素
str_num = ''.join('%s'%j for j in list1)    #遍历list1的元素，把它转化成字符串
print(str_num)