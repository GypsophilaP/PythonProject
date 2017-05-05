# -*- coding: utf-8 -*-
# 很重要不加连注释不是中文都不行
a = 100
if a >= 0:
    print a
else:
    print -a
# this is python interpreter
print 'I\'m \"OK\"'
print r'///t///'
# r'' 表示内部不转义
print '''line1
line2
line3'''
print 'Hello,%s' % 'world'
print 'Hi,%s,you have $%d' % ('chen',100000)
classmates = ['chen','ren','xuan']
print classmates
len(classmates)
classmates[1]
classmates[-1]
TuplePeople = ('Li','Chen','Ren')
print TuplePeople
sum = 0
for x in range(100):
        sum = sum + x;
print sum
d = {'Chen':100,'Ren':99,'Li':98}
print(d['Chen'])