# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 11:17:05 2019

@author: Administrator
"""

# 几进制数 转换成 十进制数 ，都是用 int()  函数 。
# 之后后面的 第二个参数 写清楚 前面字符串 是 几进制数就可以 。
# 注意一定要合法。 比如2进制数就不能出现2这样的字符。

#十进制转为二进制
print(bin(10))

#二进制转为十进制
print(int("1000000",2))

#十进制转为八进制
print(oct(11))

#八进制转为十进制
print(int('77',8))

#十进制转为十六进制
print(hex(10))

#十六进制转为十进制
print(int('0xf',16))

# oct 函数 可将任意进制的数 转换成 8进制的。
print(oct(11))
print(oct(0b1010))
print(oct(0xf))