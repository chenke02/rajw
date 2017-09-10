# -*- coding: utf-8 -*-
# author:chenke

from xlwt import *
import xlwt
from method import select
from method import week
from method import show
from method import lesson
import os

# 选取最大周数
values = select()
max1 = 0
for i in xrange(len(values)):
    max2 = max(week(values[i][2]))
    max1 = max(max1, max2)
print max1

for inputs in xrange(1, max1+1):
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
    first_style = xlwt.easyxf('font:height 10;align: wrap on;')
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
    q = u"实训楼值班表第"+str(inputs)+u"周"
    # 写入前两格
    ws.write_merge(0, 0, 1, 6, q, style9)
    ws.write(1,1,'',style4)
    ws.write(2,1,'',style4)
    # 合并单元格
    ws.write_merge(1,1,2,6,u'上午8:30之前开门，11:50关门；下午13:00之前开门,16:20关门',style0)
    # 写入星期
    a = [u'星期一', u'星期二', u'星期三', u'星期四', u'星期五']
    for i in xrange(len(a)):
        ws.write(2, 2+i, a[i], style4)

    b=[u'白天'+u'\n'+u'(1-9节)', u'晚上'+u'\n'+u'(10-13节)']
    for i in xrange(len(b)):
        ws.write(3+i, 1, b[i], style4)
    ws.write_merge(5, 5, 1, 6, u'注意:', style8)
    ws.write_merge(6, 6, 1, 6, u'       1,关门前，检查门窗，将门窗上锁！！',style8)
    ws.write_merge(7, 7, 1, 6, u'       2,有贵重物品的实训楼，请提早锁好门窗！！！',style8)


    # 定义五个数组
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
    values = select()
    for i in xrange(len(values)):
        for wek in week(values[i][2]):
            if wek == inputs:
                if lesson(values[i][3]) == u'1' or lesson(values[i][3]) == u'2' or lesson(values[i][3]) == u'3' or lesson(values[i][3]) == u'4' or lesson(values[i][3]) == u'5':
                    if values[i][3].find(u'一')!=-1:
                        print 1
                        A1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'二')!=-1:
                        print 2
                        B1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'三')!=-1:
                        print 3
                        C1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'四')!=-1:
                        D1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                        print 4
                    elif values[i][3].find(u'五')!=-1:
                        print 5
                        E1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                elif lesson(values[i][3]) == u'6' or lesson(values[i][3]) == u'7' or lesson(values[i][3]) == u'8' or lesson(values[i][3]) == u'9':
                    if values[i][3].find(u'一')!=-1:
                        print 6
                        A1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'二')!=-1:
                        print 7
                        B1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'三')!=-1:
                        print 8
                        C1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'四')!=-1:
                        print 9
                        D1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'五')!=-1:
                        print 10
                        E1.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                elif lesson(values[i][3]) == u'10' or lesson(values[i][3]) == u'11' or lesson(values[i][3]) == u'12' or lesson(values[i][3]) == u'13':
                    if values[i][3].find(u'一')!=-1:
                        print 11
                        A3.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'二')!=-1:
                        print 12
                        B3.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'三')!=-1:
                        print 13
                        C3.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'四')!=-1:
                        print 14
                        D3.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
                    elif values[i][3].find(u'五')!=-1:
                        print 15
                        E3.append(values[i][1][0:len(values[i][1])-4]+u'楼'+u'\n')
    A11=[]
    A33=[]
    B11=[]
    B33=[]
    C11=[]
    C33=[]
    D11=[]
    D33=[]
    E11=[]
    E33=[]
    # 去重
    for id in A1:
        if id not in A11:
            A11.append(id)

    for id in A3:
        if id not in A33:
            A33.append(id)
    for id in B1:
        if id not in B11:
            B11.append(id)

    for id in B3:
        if id not in B33:
            B33.append(id)
    for id in C1:
        if id not in C11:
            C11.append(id)

    for id in C3:
        if id not in C33:
            C33.append(id)
    for id in D1:
        if id not in D11:
            D11.append(id)

    for id in D3:
        if id not in D33:
            D33.append(id)
    for id in E1:
        if id not in E11:
            E11.append(id)

    for id in E3:
        if id not in E33:
            E33.append(id)

    # 从小到大函数
    A11 = show(A11)
    A33 = show(A33)
    B11 = show(B11)
    B33 = show(B3)
    C11 = show(C11)
    C33 = show(C3)
    D11 = show(D11)
    D33 = show(D3)
    E11 = show(E11)
    E33 = show(E3)

    # 数据写入excel
    ws.write(3, 2, A11, style6)
    ws.write(4, 2, A33, style6)
    ws.write(3, 3, B11, style6)
    ws.write(4, 3, B33, style6)
    ws.write(3, 4, C11, style6)
    ws.write(4, 4, C33, style6)
    ws.write(3, 5, D11, style6)
    ws.write(4, 5, D33, style6)
    ws.write(3, 6, E11, style6)
    ws.write(4, 6, E33, style6)
    # 保存excel
    a = os.getcwd().decode('gb2312')+u"/实训开关门/实训楼值班表第"+str(inputs)+u"周.xls"
    w.save(a)
