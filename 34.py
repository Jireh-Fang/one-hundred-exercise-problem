# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 10:31:27 2019

@author: Administrator
"""

#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
#完全平方指用一个整数乘以自己例如1*1，2*2，3*3等，依此类推。若一个数能表示成某个整数的平方的形式，
#则称这个数为完全平方数。完全平方数是非负数。

import math
a = True
i = 0
while a:
    num1= i + 100
    sqrt1 = math.sqrt(num1)
    num2= i + 168
    sqrt2 = math.sqrt(num2)
    if sqrt1.is_integer() and sqrt2.is_integer():
        print(i)
        a = False
    else:
        i += 1
    
    