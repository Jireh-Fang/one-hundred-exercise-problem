# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:44:18 2019

@author: Administrator
"""

#奖金提成
def reward(I):
    if I <= 10:
        return I*0.1
    elif 10 < I <= 20:
        return 10*0.1 + (I-20)*0.075
    elif 20 < I <= 40:
        return 10*0.1 + 20*0.075 + (I-20)*0.05
    elif 40 < I <= 60:
        return 10*0.1 + 20*0.075 + 20*0.05 + (I-40)*0.03
    elif 60 < I <= 100:
        return 10*0.1 + 20*0.075 + 20*0.05 + 20*0.03 + (I-60)*0.015
    else:
        return 10*0.1 + 20*0.075 + 20*0.05 + 20*0.03 + 40*0.015 + (I-100)*0.01

print(reward(72))