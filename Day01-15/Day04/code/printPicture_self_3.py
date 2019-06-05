#coding=utf-8

rank = int(input('输入行数'))
type = raw_input('left or middle or right')
if type == 'left':
    for x in range(1,rank + 1):
        for i in range(1,x+1):
            print '*',
        print '\n'
if type == 'right':
    for x in range(1,rank + 1):
        for i in range(1,rank - x + 1):
            print ' ',
        for j in range(1,x + 1):
            print '*',
        print '\n'
if type == 'middle':
    for x in range(1,rank + 1):
        for i in range(1,rank - x + 1):
            print ' ',
        for j in range(1,x * 2):
            print '*',
        for i in range(1,rank - x + 1):
            print ' ',
        print '\n'