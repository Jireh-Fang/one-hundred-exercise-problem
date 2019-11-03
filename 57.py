# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:07:22 2019

@author: Administrator
"""

#判断一个数是不是质数
count = 0
for i in range(100,201):
    time = 0
    for j in range(1,i+1):
        if i%j == 0:
            time += 1
    if time == 2:
        count += 1
        print('%s'%i)
print('一共有%d个质数'%count)