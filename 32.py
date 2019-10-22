# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 22:03:44 2019

@author: Administrator
"""

#3*3乘法口诀表
for i in range(1,4):
    for j in range(1,i+1):
        print('{}×{}={}'.format(i,j,i*j),end=' ')
    print()