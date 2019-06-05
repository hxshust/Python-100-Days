#coding=utf-8
import math
global approximate_number
global multiple_number
number1 = int(input('输入数字1'))
number2 = int(input('输入数字2'))
min_number = min(number1,number2)
# approximate_number = 1
max_number = max(number1,number2)
for x in range(1,min_number+1):
    if number1 % x == 0 and number2 % x == 0:
        approximate_number = x

for x in range(max_number,number1 * number2 + 1):
    if x % number1 == 0 and x % number2 == 0:
        multiple_number = x
        break
print '最大公约数是 ', approximate_number
print '最小公倍数是 ', multiple_number



