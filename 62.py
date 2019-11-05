# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:05:30 2019

@author: Administrator
"""

#这个题换成xyz的排列问题就好理解了，不用去理会abc,第一位不是x,最后一位不是x和z就可以了
from itertools import permutations
team1=['a','b','c']
team2=['x','y','z']

#通过permutations获取team2的全排列情况
team=list(permutations(team2,3))
for n in team:
    # 当排列的情况满足第一位不是x,最后一位不是x和z时，则是符合要求的
    if n[0]!='x'and n[2]!='x' and n[2]!='z':
        for i in range(3):
            print('%s--%s'%(team1[i],n[i]))