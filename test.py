# -*- coding: utf-8 -*-
# author:chenke

import xlwt
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('sheet1')
first_col=sheet.col(0)
sec_col=sheet.col(1)

first_col.width=256*20
tall_style = xlwt.easyxf('font:height 720;align: wrap on;') # 36pt,类型小初的字号
sheet.write(1,1,u'你好'+'\n'+u'你好', tall_style)


book.save('width.xls')