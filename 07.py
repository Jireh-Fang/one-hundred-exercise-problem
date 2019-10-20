# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:00:46 2019

@author: Administrator
"""

#读取7个数（1-50）的整数值，每读取一个数，程序打印出该值个数的*
from random import randint
for i in range(7):
    num = randint(1,50)
    print('*'*num)