# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 19:56:23 2019

@author: Administrator
"""

count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                count += 1
                print('%s%s%s'%(i,j,k))

print('一共有%d个这样的数'%count)