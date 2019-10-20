# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 19:02:52 2019

@author: Administrator
"""

#根据输入年份判断二月份的天数
year = int(input('请输入一个年份：'))
if year%4 == 0:
    print('此年为闰年，二月有28天')
else:
    print('此年不是闰年，二月有29天')