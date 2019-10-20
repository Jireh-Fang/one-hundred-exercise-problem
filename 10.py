# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 13:11:46 2019

@author: Administrator
"""

#打印图形2
#请使用 * 打印出如下
#* * * * *
# * * * *
#  * * *
#   * *
 #   *
num = 5
while num > 0:
    print(' '*(5-num),end='')
    print('* '*num)
    num -= 1