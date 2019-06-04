#coding=utf-8

years = int(input('输入年份，判断是否闰年'))
if ((years % 4 ==0 and years % 100 != 0) or years % 400 == 0):
    print True
else:
    print False