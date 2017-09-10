# -*- coding: utf-8 -*-
# author:chenke

from xlwt import *
import xlwt
from method import select
from method import week
from method import show
from method import lesson
import os

while(True):
    # 输入第几周:
    inputs = input("input:")
    # 打开excel
    w=Workbook()
    ws = w.add_sheet(u'值班')
    # 第一列宽
    first_col=ws.col(0)
    first_col.width=256*2
    # 第二列宽
    second_col=ws.col(1)
    second_col.width=256*11
    # 星期一到星期五列宽
    for i in xrange(5):
        j=i+2
        col=ws.col(j)
        col.width=256*23
    # 第一行高
    first_style = xlwt.easyxf('font:height 10;')
    style0 = xlwt.easyxf('font:height 300;align:horiz center,vert center,wrap on; borders:left THIN,right THIN,top THIN,bottom THIN')
    style=xlwt.easyxf('font:height 300;align: wrap on;')
    style1 = xlwt.easyxf('font:height 800;align: wrap on;')
    style4=xlwt.easyxf('borders:left THIN,right THIN,top THIN,bottom THIN;align:horiz center,vert center,wrap on;font:bold on,height 0xF0;')
    style5=xlwt.easyxf('borders:left THIN,right THIN,top THIN,bottom THIN;align:wrap on,vert center;font:height 0xD0;')
    style6=xlwt.easyxf('borders:left THIN,right THIN,top THIN,bottom THIN;align:wrap on,horiz left,vert top;font:height 0xD0;')
    style7=xlwt.easyxf('borders:left THIN,right THIN,top THIN,bottom THIN;align:wrap on,horiz center,vert center;font:height 0xD0;')
    style8=xlwt.easyxf('align:horiz left,vert center;font:height 0xA0;')
    style9=xlwt.easyxf('align:horiz center,vert center;font:height 500;')
    first_row = ws.row(0)
    first_row.set_style(first_style)
    ws.row(1).set_style(style)
    ws.row(2).set_style(style)
    ws.row(5).set_style(style)
    ws.row(6).set_style(style)
    q = u"教学统计第"+str(inputs)+u"周"
    ws.write_merge(0, 0, 1, 6, q, style9)
    # 写入星期
    ws.write(1, 1, '', style4)
    a = [u'星期一', u'星期二', u'星期三', u'星期四', u'星期五']
    for i in xrange(len(a)):
        ws.write(1, 2+i, a[i], style4)

    b=[u'白天'+u'\n'+u'(1-5节)',u'下午'+u'\n'+u'(6-9节)', u'晚上'+u'\n'+u'(10-13节)']
    ws.write(2, 1, b[0], style4)
    ws.write(3, 1, u'合计', style4)
    ws.write(4, 1, b[1], style4)
    ws.write(5, 1, u'合计', style4)
    ws.write(6, 1, b[2], style4)
    ws.write(7, 1, u'合计', style4)

    # 定义五个数组
    A1=[]
    A2=[]
    A3=[]

    B1=[]
    B2=[]
    B3=[]

    C1=[]
    C2=[]
    C3=[]

    D1=[]
    D2=[]
    D3=[]

    E1=[]
    E2=[]
    E3=[]

    # 分发数据到对应数组
    values = select()
    for i in xrange(len(values)):
        for wek in week(values[i][3]):
            if wek == inputs:
                if lesson(values[i][4]) == u'1' or lesson(values[i][4]) == u'2' or lesson(values[i][4]) == u'3' or lesson(values[i][4]) == u'4' or lesson(values[i][4]) == u'5':
                    if values[i][4].find(u'一')!=-1:
                        print 1
                        A1.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'二')!=-1:
                        print 2
                        B1.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'三')!=-1:
                        print 3
                        C1.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'四')!=-1:
                        D1.append(values[i][1]+u'\n')
                        print 4
                    elif values[i][4].find(u'五')!=-1:
                        print 5
                        E1.append(values[i][1]+u'\n')
                elif lesson(values[i][4]) == u'6' or lesson(values[i][4]) == u'7' or lesson(values[i][4]) == u'8' or lesson(values[i][4]) == u'9':
                    if values[i][4].find(u'一')!=-1:
                        print 6
                        A2.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'二')!=-1:
                        print 7
                        B2.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'三')!=-1:
                        print 8
                        C2.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'四')!=-1:
                        print 9
                        D2.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'五')!=-1:
                        print 10
                        E2.append(values[i][1]+u'\n')
                elif lesson(values[i][4]) == u'10' or lesson(values[i][4]) == u'11' or lesson(values[i][4]) == u'12' or lesson(values[i][4]) == u'13':
                    if values[i][4].find(u'一')!=-1:
                        print 11
                        A3.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'二')!=-1:
                        print 12
                        B3.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'三')!=-1:
                        print 13
                        C3.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'四')!=-1:
                        print 14
                        D3.append(values[i][1]+u'\n')
                    elif values[i][4].find(u'五')!=-1:
                        print 15
                        E3.append(values[i][1]+u'\n')
    A11=[]
    A22=[]
    A33=[]
    B11=[]
    B22=[]
    B33=[]
    C11=[]
    C22=[]
    C33=[]
    D11=[]
    D22=[]
    D33=[]
    E11=[]
    E22=[]
    E33=[]
    # 去重
    for id in A1:
        if id not in A11:
            A11.append(id)

    for id in A2:
        if id not in A22:
            A22.append(id)

    for id in A3:
        if id not in A33:
            A33.append(id)
    for id in B1:
        if id not in B11:
            B11.append(id)

    for id in B2:
        if id not in B22:
            B22.append(id)

    for id in B3:
        if id not in B33:
            B33.append(id)
    for id in C1:
        if id not in C11:
            C11.append(id)

    for id in C2:
        if id not in C22:
            C22.append(id)

    for id in C3:
        if id not in C33:
            C33.append(id)
    for id in D1:
        if id not in D11:
            D11.append(id)

    for id in D2:
        if id not in D22:
            D22.append(id)

    for id in D3:
        if id not in D33:
            D33.append(id)
    for id in E1:
        if id not in E11:
            E11.append(id)

    for id in E2:
        if id not in E22:
            E22.append(id)

    for id in E3:
        if id not in E33:
            E33.append(id)


    # 数据写入excel
    ws.write(2, 2, A11, style6)
    ws.write(3, 2, len(A11), style6)
    ws.write(4, 2, A22, style6)
    ws.write(5, 2, len(A22), style6)
    ws.write(6, 2, A33, style6)
    ws.write(7, 2, len(A33), style6)
    ws.write(2, 3, B11, style6)
    ws.write(3, 3, len(B11), style6)
    ws.write(4, 3, B22, style6)
    ws.write(5, 3, len(B22), style6)
    ws.write(6, 3, B33, style6)
    ws.write(7, 3, len(B33), style6)
    ws.write(2, 4, C11, style6)
    ws.write(3, 4, len(C11), style6)
    ws.write(4, 4, C22, style6)
    ws.write(5, 4, len(C22), style6)
    ws.write(6, 4, C33, style6)
    ws.write(7, 4, len(C33), style6)
    ws.write(2, 5, D11, style6)
    ws.write(3, 5, len(D11), style6)
    ws.write(4, 5, D22, style6)
    ws.write(5, 5, len(D22), style6)
    ws.write(6, 5, D33, style6)
    ws.write(7, 5, len(D33), style6)
    ws.write(2, 6, E11, style6)
    ws.write(3, 6, len(E11), style6)
    ws.write(4, 6, E22, style6)
    ws.write(5, 6, len(E22), style6)
    ws.write(6, 6, E33, style6)
    ws.write(7, 6, len(E33), style6)
    # 保存excel
    print os.getcwd().decode('gb2312')
    a = os.getcwd().decode('gb2312')+u"/教学班车/教学统计第"+str(inputs)+u"周.xls"
    w.save(a)
