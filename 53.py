# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:25:08 2019

@author: Administrator
"""

#第n个斐波那契数
def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

print(Fibonacci(10))
    
    
    