#coding=utf-8
import math

global result
number = int(input('输入一个大于等于2的正整数'))
if number <= 1:
    print 'valid number'
elif number == 2 or number == 3:
    result = True
else:
    number_sqrt = int(math.sqrt(number))
    count = 2
    while count <= number_sqrt:
        if number%count == 0:
            result = False
            break
        else:
            count = count + 1;
        result = True

    print '是否是素数的结果是 ' , result


