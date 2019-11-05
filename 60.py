# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:56:36 2019

@author: Administrator
"""


#递归返回每次反弹的高度
def fn(n):
    if n==1:
        return 50
    else:
        return fn(n-1)/2
distance=0
for i in range(1,11):
    if i == 10:
        distance+=2*fn(i)
    else:
        distance+=3*fn(i)

print('第十次落地一共经过了%s米。\n第十次反弹了%s米。'%(distance,fn(10)))
    