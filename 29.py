# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:04:49 2019

@author: Administrator
"""

#输出1000~2000之间的闰年
for year in range(1000,2001):
    if year%4 == 0:
        print(year)