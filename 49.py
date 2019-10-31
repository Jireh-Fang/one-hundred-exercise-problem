# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 10:17:17 2019

@author: Administrator
"""

#算两数的最小公倍数
def lcm(num1,num2):
    num = num1*num2
    i = 1
    a = True
    while a or i<=(num1*num2):
        if i%num1 == 0 and i%num2 == 0:
            a = False
            return i
        else:
            i += 1

print(lcm(24,12))
            
        
            