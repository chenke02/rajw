# -*- coding: utf-8 -*-
# author:chenke


from method import insert
from method import Build
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
from method import lesson
from method import show
from method import week

# 初始化数据库
Build()
# #——————登录教室页面——————
dr = webdriver.Firefox()
dr.get("http://10.10.1.7:8080/")
time.sleep(1)
dr.maximize_window()
time.sleep(1)
dr.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/a").click()
time.sleep(1)

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
        # 选中节次
        jieci = dr.find_elements_by_xpath("/html/body/table/tbody/tr/td/table[3]/tbody/tr/td[13]")
        for i in range(len(zhouci)):
            z=zhouci[i].text
            j=jieci[i].text
            if z != u'周次':
                insert(k, z, j)
        # 退出iframe
        time.sleep(1)
        dr.switch_to.default_content()
        print k[0:len(k)-4]+u'楼'
