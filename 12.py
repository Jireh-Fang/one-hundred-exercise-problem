# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:55:45 2019

@author: Administrator
"""

#输入3个整数a,b,c，按大小顺序输出
list_num = []
a = int(input('请依次输入三个整数,第一个为：'))
b = int(input('第二个为：'))
c = int(input('第三个为：'))
list_num.append(a)
list_num.append(b)
list_num.append(c)
sorted_list_num = sorted(list_num)
for i in sorted_list_num:
    print(i)