# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:19:41 2019

@author: Administrator
"""

#9*9乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        print('{}×{}={}'.format(i,j,i*j),end=' ')
    print()