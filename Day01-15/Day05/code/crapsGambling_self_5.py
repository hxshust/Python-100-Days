#coding=utf-8

from random import randint
global money
money = 100
print 'your money =',money
while money > 0:
    stake = int(input('请下注：'))
    a = randint(1, 6)
    b = randint(1, 6)
    print '你掷出的点数是',a + b
    if a + b == 7 or a + b == 11:
        money = money + stake
        print 'you win!','you money =',money
    elif a + b == 2 or a + b == 3 or a + b == 12:
        money = money - stake
        print 'you lose!','you money =',money
    else:
        print '目前点数是',a + b
        stake2 = int(input('目前可加注'))
        while True:
            c = randint(1,6) + randint(1,6)
            print '你掷出了',c,'点'
            if c == 7:
                money = money - stake2 - stake
                print 'you finally lose!','your money =',money
                break
            elif c == a + b:
                money = money + stake2 + stake
                print 'you finaly win!','your money =',money
                break
print '你破产了' 