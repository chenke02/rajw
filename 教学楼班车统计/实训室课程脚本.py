# -*- coding: utf-8 -*-
# author:chenke

import time

from xlwt import *
import xlwt
from selenium.webdriver.support.select import Select
from selenium import webdriver

from test.shixunshi.method import lesson
from test.shixunshi.method import show
from test.shixunshi.method import week


# 输入第几周:
inputs = input("input:")
# #——————登录教室页面——————
dr = webdriver.Firefox()
dr.get("http://10.10.1.7:8080/")
time.sleep(1)
dr.maximize_window()
time.sleep(1)
dr.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/a").click()
time.sleep(1)

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
style0 = xlwt.easyxf('font:height 300;align:horiz center,vert center; borders:left THIN,right THIN,top THIN,bottom THIN')
style=xlwt.easyxf('font:height 300;')
style1 = xlwt.easyxf('font:height 800;')
style4=xlwt.easyxf('borders:left THIN,right THIN,top THIN,bottom THIN;align:horiz center,vert center;font:bold on,height 0xF0;')
style5=xlwt.easyxf('borders:left THIN,right THIN,top THIN,bottom THIN;align:horiz left,vert center;font:height 0xD0;')
style6=xlwt.easyxf('borders:left THIN,right THIN,top THIN,bottom THIN;align:horiz left,vert top;font:height 0xD0;')
style7=xlwt.easyxf('borders:left THIN,right THIN,top THIN,bottom THIN;align:horiz center,vert center;font:height 0xD0;')
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
##——————填表单——————
# 得到当前窗口的句柄
dr.switch_to_window(dr.window_handles[-1])
# 选中格式二
dr.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr/td/input[2]").click()
# 选校区
Select(dr.find_element_by_name("Sel_XQ")).select_by_visible_text(u"瑞安学院")
time.sleep(1)

for i in xrange(5,9):
    # 选实训楼
    time.sleep(1)
    Select(dr.find_element_by_id("Sel_JXL")).select_by_index(i)
    time.sleep(1)
    lj=len(dr.find_elements_by_xpath("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[5]/select/option"))
    shixunlou=dr.find_elements_by_xpath("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td/table/tbody/tr/td[5]/select/option")
    time.sleep(1)
    for j in xrange(1, lj):
        # 选对应实训楼号码
        time.sleep(1)
        Select(dr.find_element_by_id("Sel_ROOM")).select_by_index(j)
        k=shixunlou[j].text
        time.sleep(1)
        # 输入验证码
        time.sleep(5)
        # 检索
        dr.find_element_by_name("btnSearch").click()
        time.sleep(1)

        # #—————打印数据———————
        # 进入iframe
        iframe=dr.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/iframe[2]")
        Iframe = dr.switch_to_frame(iframe)
        # tr标签的数量
        tr=len(dr.find_elements_by_xpath("/html/body/table/tbody/tr/td/table[3]/tbody/tr"))
        # 选中周次
        zhouci=dr.find_elements_by_xpath("/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[12]")
        Z=[]
        J=[]
        for zhou in zhouci[1:len(zhouci)]:
            z=zhou.text
            Z.append(z)
        # 选中节次
        jieci = dr.find_elements_by_xpath("/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[13]")
        for jie in jieci[1:len(jieci)]:
            j=jie.text
            print j
            J.append(j)
        # 退出iframe
        time.sleep(1)
        dr.switch_to.default_content()
        print k[0:len(k)-4]+u'楼'
        # 分发数据到对应数组
        for i in xrange(len(Z)):
            for wek in week(Z[i]):
                if wek == inputs:
                    if lesson(J[i]) == u'1' or lesson(J[i]) == u'2' or lesson(J[i]) == u'3' or lesson(J[i]) == u'4' or lesson(J[i]) == u'5':
                        if J[i].find(u'一')!=-1:
                            print 1
                            A1.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'二')!=-1:
                            print 2
                            B1.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'三')!=-1:
                            print 3
                            C1.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'四')!=-1:
                            D1.append(k[0:len(k)-4]+u'楼'+u'\n')
                            print 4
                        elif J[i].find(u'五')!=-1:
                            print 5
                            E1.append(k[0:len(k)-4]+u'楼'+u'\n')
                    elif lesson(J[i]) == u'6' or lesson(J[i]) == u'7' or lesson(J[i]) == u'8' or lesson(J[i]) == u'9':
                        if J[i].find(u'一')!=-1:
                            print 6
                            A1.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'二')!=-1:
                            print 7
                            B1.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'三')!=-1:
                            print 8
                            C1.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'四')!=-1:
                            print 9
                            D1.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'五')!=-1:
                            print 10
                            E1.append(k[0:len(k)-4]+u'楼'+u'\n')
                    elif lesson(J[i]) == u'10' or lesson(J[i]) == u'11' or lesson(J[i]) == u'12' or lesson(J[i]) == u'13':
                        if J[i].find(u'一')!=-1:
                            print 11
                            A3.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'二')!=-1:
                            print 12
                            B3.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'三')!=-1:
                            print 13
                            C3.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'四')!=-1:
                            print 14
                            D3.append(k[0:len(k)-4]+u'楼'+u'\n')
                        elif J[i].find(u'五')!=-1:
                            print 15
                            E3.append(k[0:len(k)-4]+u'楼'+u'\n')
        print A1, B1, C1, D1, E1
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
a = u"G:/Solidworks2017/作品/勤工俭学/实训楼值班表第"+str(inputs)+u"周.xls"
w.save(a)