# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:25:42 2019

@author: Administrator
"""

tmpStr = input('请输入字符串：')
alphaNum=0
numbers=0
spaceNum=0
otherNum=0
for i in tmpStr:      
    if i.isalpha():         #判断是不是中英文字母
        alphaNum +=1         
    elif i.isnumeric():     #判断是不是数字
        numbers +=1
    elif i.isspace():       #判断是不是空格
        spaceNum +=1
    else:
        otherNum +=1
print('字母=%d'%alphaNum)
print('数字=%d'%numbers)
print('空格=%d'%spaceNum)
print('其他=%d'%otherNum)