#coding=utf-8

import math

a = float(input('输入三角形的一个边长'))
b = float(input('输入三角形的一个边长'))
c = float(input('输入三角形的一个边长'))

p = (a + b + c)/2
if a < p and b < p and c < 8:
    print '可构成三角形，海伦公式计算面积'
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print '面积为 ' , area
else:
    print '无法构成三角形'

 
