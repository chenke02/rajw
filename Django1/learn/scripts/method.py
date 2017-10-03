# -*- coding: utf-8 -*-
# author:chenke

import re

# 每节课截取处理函数
def lesson(a):
    str = re.split('-|\[', a)
    return str[1]


# 对实训楼房间排序
# noinspection PyInterpreter
def show(args):
    a11=[]
    for i in xrange(len(args)):
        t=args[i][3:8]
        n = re.split(u'-|,', t)
        a11.append(n[0]+n[1])
    tt = {'a': a11, 'b': args}
    for i in range(0, len(a11)):
        for j in range(i+1, len(a11)):
            if a11[i] > a11[j]:
                a11[i], a11[j] = a11[j], a11[i]
                tt['b'][i], tt['b'][j] = tt['b'][j], tt['b'][i]
    return tt['b']


# 将周次处理成数组并从小到大排列函数
def week(a):
    c = []
    strs = a.split(u',')
    for str in strs:
        if str.find(u'-') != -1:
            b = str.split(u'-')
            for bs in xrange(int(b[0]), int(b[1])+1):
                c.append(bs)
        else:
            c.append(int(str))
    return set(c)