# -*- coding: utf-8 -*-
# author:chenke

from django.shortcuts import render, render_to_response
from models import train_course, train_basic
from scripts.method import show, lesson



def index1_1(request):
    struct = {}
    struct['hello'] = 'python'
    return render(request, 'index1/index1-1.html', struct)

def index1_1_1(request, a, b):
    c = int(a)+int(b)
    struct = {}
    struct['hello'] = c
    return render(request, 'index1/index1-1.html', struct)


# 实训楼开关门安排表
def index5_1(request, k):
    A1=[]
    A3=[]
    B1=[]
    B3=[]
    C1=[]
    C3=[]
    D1=[]
    D3=[]
    E1=[]
    E3=[]
    # 分发数据到对应数组
    page = train_course.objects.order_by('-Week')[1].Week
    for wek in train_course.objects.filter(Week=int(k)):
        if wek.Place[0:3] == u'实训楼':
            if lesson(wek.Section) == u'1' or lesson(wek.Section) == u'2' or lesson(wek.Section) == u'3' or lesson(wek.Section) == u'4' or lesson(wek.Section) == u'5':
                if wek.Section.find(u'一') !=-1:
                    print 1
                    A1.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'二')!=-1:
                    print 2
                    B1.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'三')!=-1:
                    print 3
                    C1.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'四')!=-1:
                    D1.append(wek.Place[0:len(wek.Place)-4])
                    print 4
                elif wek.Section.find(u'五')!=-1:
                    print 5
                    E1.append(wek.Place[0:len(wek.Place)-4])
            elif lesson(wek.Section) == u'6' or lesson(wek.Section) == u'7' or lesson(wek.Section) == u'8' or lesson(wek.Section) == u'9':
                if wek.Section.find(u'一')!=-1:
                    print 6
                    A1.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'二')!=-1:
                    print 7
                    B1.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'三')!=-1:
                    print 8
                    C1.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'四')!=-1:
                    print 9
                    D1.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'五')!=-1:
                    print 10
                    E1.append(wek.Place[0:len(wek.Place)-4])
            elif lesson(wek.Section) == u'10' or lesson(wek.Section) == u'11' or lesson(wek.Section) == u'12' or lesson(wek.Section) == u'13':
                if wek.Section.find(u'一')!=-1:
                    print 11
                    A3.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'二')!=-1:
                    print 12
                    B3.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'三')!=-1:
                    print 13
                    C3.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'四')!=-1:
                    print 14
                    D3.append(wek.Place[0:len(wek.Place)-4])
                elif wek.Section.find(u'五')!=-1:
                    print 15
                    E3.append(wek.Place[0:len(wek.Place)-4])
    struct = {}
    struct['A11'] = []
    struct['A33'] = []
    struct['B11'] = []
    struct['B33'] = []
    struct['C11'] = []
    struct['C33'] = []
    struct['D11'] = []
    struct['D33'] = []
    struct['E11'] = []
    struct['E33'] = []
    # 去重
    for id in A1:
        if id not in struct['A11']:
            struct['A11'].append(id)
    for id in A3:
        if id not in struct['A33']:
            struct['A33'].append(id)
    for id in B1:
        if id not in struct['B11']:
            struct['B11'].append(id)
    for id in B3:
        if id not in struct['B33']:
            struct['B33'].append(id)
    for id in C1:
        if id not in struct['C11']:
            struct['C11'].append(id)
    for id in C3:
        if id not in struct['C33']:
            struct['C33'].append(id)
    for id in D1:
        if id not in struct['D11']:
            struct['D11'].append(id)
    for id in D3:
        if id not in struct['D33']:
            struct['D33'].append(id)
    for id in E1:
        if id not in struct['E11']:
            struct['E11'].append(id)
    for id in E3:
        if id not in struct['E33']:
            struct['E33'].append(id)
    struct['head'] = k
    struct['pages'] = xrange(1, int(page)+1)
    struct['A11'] = show(struct['A11'])
    struct['A33'] = show(struct['A33'])
    struct['B11'] = show(struct['B11'])
    struct['B33'] = show(struct['B33'])
    struct['C11'] = show(struct['C11'])
    struct['C33'] = show(struct['C33'])
    struct['D11'] = show(struct['D11'])
    struct['D33'] = show(struct['D33'])
    struct['E11'] = show(struct['E11'])
    struct['E33'] = show(struct['E33'])
    return render(request, 'index5/index5-1.html', struct)


# 实训楼课程表
def index5_2(request, d):
    struct = {}
    return render(request, 'index5/index5-2.html', struct)

# 实训楼统计
def index5_6(request):
    names = train_course.objects.all()
    return render_to_response('index5/index5-6.html', locals())

