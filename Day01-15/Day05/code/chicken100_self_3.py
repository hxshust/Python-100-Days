#coding=utf-8


for cock in range(0,20):
    for hen in range(0,(100 - 5*cock)/3+1):
        for chicken in range(0,(100 - 5*cock -3*hen)*3+1,3):
            if cock+hen+chicken == 100 and 5*cock + 3*hen + chicken/3 == 100:
                print 'cock=',cock,'hen=',hen,'chicken',chicken

