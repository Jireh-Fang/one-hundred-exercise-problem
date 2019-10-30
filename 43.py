# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:42:20 2019

@author: Administrator
"""

#d打印图形
def rectangle(length=5,width=5,sign='*'):
    for i in range(width):
        print(sign*length)

rectangle(6,8,'/')