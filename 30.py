# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:17:56 2019

@author: Administrator
"""

#输入三角形三个边求计算三角形的面积
import math
list1 = []
print('请输入三角形的三条边的边长')
a = int(input('第一条边：'))
b = int(input('第二条边：'))
c = int(input('第三条边：'))
list1.append(a)
list1.append(b)
list1.append(c)
list2 = sorted(list1)
if (list2[0]+list2[1]) > list2[2]:
    p = (list2[0]+list2[1]+list2[2])/2
    S = math.sqrt(p*(p-list2[0])*(p-list2[1])*(p-list2[2]))
    print(S)
else:
    print('此三边不能构成三角形')