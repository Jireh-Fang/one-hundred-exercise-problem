# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:39:20 2019

@author: Administrator
"""

#统计1到100中能被3整除的数的和
sum = 0
for i in range(3,101,3):
    sum += i
print(sum)


#sum = 0
#for i in range(1,101):
#    if i%3 == 0：
#        sum += i
#print(sum)