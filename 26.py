# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:43:23 2019

@author: Admin2trator
"""

#统计1到100的质数之和

#添加1-100的质数到列表中
list1 = []
for num in range(1,101):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        list1.append(num)

sum = 0
for j in list1:
    sum += j
print(sum)