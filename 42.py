# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:01:01 2019

@author: Administrator
"""

import random 
import string
a = list(string.ascii_letters)  #生成26个英文小写字母和26个大写字母
for i in range(200):
    c = []
    random.shuffle(a)          #打乱序列
    b = ''.join(a)             #列表拼成字符串
    c.append(b[:8])
    print(c)