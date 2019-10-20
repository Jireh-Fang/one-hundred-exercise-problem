# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:58:31 2019

@author: Administrator
"""

#判断闰年
year = int(input('请输入一个年份：'))
if year%4 == 0:
    print('此年为闰年')
else:
    print('此年不是闰年')