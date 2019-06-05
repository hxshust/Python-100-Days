#coding=utf-8

IN2CM = 2.54
length = float(input('输入长度'))
unit = raw_input('输入单位')
if unit == 'in' or unit == '英寸':
    length_trans = length * IN2CM
    print '该长度对应 ' , length_trans , ' cm/厘米'
elif unit == 'cm' or unit == '厘米':
    length_trans = length / IN2CM
    print  '该长度对应 ' , length_trans , ' in/英寸'
else:
    print 'Valid unit!'
    