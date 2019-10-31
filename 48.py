# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:42:07 2019

@author: Administrator
"""

def gcd(num1,num2):
    #保证num1比num2大
    if num1 >= num2:
        num1,num2=num1,num2
    else:
        num1,num2 = num2,num1
    #将num1的所有约数放入list1，将num2所有约数放入list2
    list1 = []
    list2 = []
    for i in range(1,num1+1):
        if num1%i == 0:
            list1.append(i)
    for j in range(1,num2+1):
        if num2%j == 0:
            list2.append(j)
    #判断list2的约数是否在list1中
    a = True
    index1 = -1
    while a or index >= -(len(list2)-1) :
        if list2[index1] in list1:
            a = False
            return list2[index1]
        else:
            index1 -= 1


print(gcd(96,36))
            
    
        
            