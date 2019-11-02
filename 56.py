# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 20:05:25 2019

@author: Administrator
"""

def fn(n):
    if n<3:
        return 1
    else:
        return fn(n-1)+fn(n-2)
print('第十个月兔子的数量为：%s只'%(2*fn(10)))