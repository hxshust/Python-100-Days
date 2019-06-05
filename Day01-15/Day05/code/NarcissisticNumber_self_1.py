#coding=utf-8

for i in range(100,1000):
    i1 = i // 100
    i2 = (i - i1 * 100) // 10
    i3 = i - i1 * 100 - i2 * 10

    if (i1**3 + i2**3 + i3**3) == i:
        print '***' ,i,'***' 

