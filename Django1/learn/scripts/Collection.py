# -*- coding: utf-8 -*-
# author:chenke


import time
from selenium.webdriver.support.select import Select
from selenium import webdriver
from learn.models import train_course


def Collection():
    train_course.objects.all().delete()
    # #——————登录教室页面——————
    dr = webdriver.Firefox()
    dr.get("http://10.10.1.7:8080/")
    time.sleep(1)
    dr.maximize_window()
    time.sleep(1)
    dr.find_element_by_xpath("/html/body/table/tbody/tr[2]/td/table/tbody/tr[3]/td[1]/div[2]/table/tbody/tr[2]/td/div/table/tbody/tr/td/table/tbody/tr[6]/td[2]/a").click()
    time.sleep(1)

    ##——————填表单——————
    # 得到当前窗口的句柄
    dr.switch_to_window(dr.window_handles[-1])
    # 选中格式二
    dr.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td/table/tbody/tr/td[1]/input[1]").click()
    # 选校区
    Select(dr.find_element_by_name("Sel_XQ")).select_by_visible_text(u"瑞安学院")
    time.sleep(1)
    trs = len(dr.find_elements_by_xpath("/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr/td[2]/select/option"))
    print trs

    for i in xrange(0, trs-1):
        # 选实训楼
        time.sleep(1)
        Select(dr.find_element_by_name("Sel_ZC")).select_by_index(i)
        # 输入验证码
        time.sleep(5)
        # 检索
        dr.find_element_by_name("btnseach").click()
        time.sleep(1)

        # #—————打印数据———————
        # 进入iframe
        iframe=dr.find_element_by_xpath("/html/body/form/table/tbody/tr[3]/td/iframe[4]")
        dr.switch_to_frame(iframe)
        # 标签长度
        pages = len(dr.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[2]"))
        # 选中课程
        sections = dr.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[2]")
        # 选中人数
        peoples = dr.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[4]")
        # 选中任课老师
        teachers = dr.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[5]")
        # 选中节次
        weeks = dr.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[6]")
        # 选中地点
        places = dr.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[7]")
        # 选中班级
        classes = dr.find_elements_by_xpath("/html/body/table[2]/tbody/tr/td[8]")
        # 课程数组
        w = []
        # 人数数组
        p = []
        for j in xrange(pages):
            w.append(sections[j].text)
            if w[j] == u'':
                w[j] = w[j-1]
            p.append(peoples[j].text)
            if p[j] == u'':
                p[j] = p[j-1]
            teacher = teachers[j].text
            week = weeks[j].text
            place = places[j].text
            Class = classes[j].text
            if week != u'节次':
                train_course.objects.create(Course=w[j], People=p[j], Teacher=teacher, Section=week, Place=place, Classes=Class, Week=i+1)
        # 退出iframe
        time.sleep(1)
        dr.switch_to.default_content()
