# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 14:00:28 2019

@author: Administrator
"""

for i in range(100,1000):
    s = str(i)
    one = int(s[-1])
    ten = int(s[-2])
    hun = int(s[-3])
    if i == one**3 + ten**3 + hun**3:
        print(i)