# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 17:01:47 2019

@author: Administrator
"""

#判断一个数是不是质数
num = int(input('请输入一个数：'))
count = 0
for i in range(1,num+1):
    if num%i == 0:
        count += 1
if count == 2:
    print('该数是质数')
else:
    print('该数不是质数')