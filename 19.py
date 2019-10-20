# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:53:04 2019

@author: Administrator
"""

#用高斯算法统计1到100之和
list1 = [i for i in range(1,101)]
sum = ((list1[0]+list1[-1])*len(list1))/2
print(sum)