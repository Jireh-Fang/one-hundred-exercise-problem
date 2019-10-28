# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 12:09:43 2019

@author: Administrator
"""

while True:
    num = int(input('按1开始，按0退出\n'))
    if num == 1:
        while True:
            year = int(input('请输入年：'))
            month = int(input('请输入月：'))
            day = int(input('请输入日：'))
        
            count = 0    #计算总天数
            total = 0    #累加天数
            days = [31,28,31,30,31,30,31,31,30,31,30,31]    #每月天数
        
            for i in range(month-1):
                total += days[i]
                count = total+day        
            else:
                count = total+day
                
                if year%100 != 0 and year%4 == 0 or year%400 == 0:    #判断闰年，2月天数加1天
                    if month > 2:    
                        count += 1
            break
        print('%d年%d月%d日是这一年的第%d天'%(year,month,day,count))
    else:
        break
