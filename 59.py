# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:04:43 2019

@author: Administrator
"""


for i in range(1,1000):
    sum = 0
    list1 = []
    for j in range(1,i):
        if i%j == 0:
            list1.append(j)   #将除了自身之外的因数添加到列表中
    for k in list1:
        sum += k
    if i == sum:
        print(i)