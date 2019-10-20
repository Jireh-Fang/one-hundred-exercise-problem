# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 14:24:00 2019

@author: Administrator
"""

#输入数字，将3个偶数加入列表并按从小到大排序

#Q：输入3个整数a,b,c，判断是否为偶数，是则加入列表，列表满三个元素则程序退出并按从小到大顺序输出
list1 = []
while len(list1) < 3:
    num = int(input('请输入一个数字：'))
    if num%2 == 0:
        list1.append(num)
list2 = sorted(list1)
for i in list2:
    print(i)