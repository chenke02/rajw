# -*- coding: utf-8 -*-
# author:chenke

import re
import sqlite3

#创建数据库
def Build():
    conn = sqlite3.connect("build.db")
    print 'Opened database1 successfully'
    conn.execute('''create table if not exists CNAME(
      ID INTEGER PRIMARY KEY AUTOINCREMENT,
      NAME             nvarchar     NOT NULL,
      CLASS            VARCHAR     NOT NULL,
      ZHOUCI           VARCHAR    NOT NULL,
      JIECI            VARCHAR     NOT NULL
      );''')
    print 'Table1 created successfully'
    #向表中插入记录
    return conn

#插入CNAME数据库
def insert(a,b,c,d):
    conn = sqlite3.connect("build.db")
    cursor = conn.cursor()
    # 注意sql语句中使用了格式化输出的占位符%s和%d来表示将要插入的变量，其中%s需要加引号''
    cursor.execute("insert into CNAME(NAME,CLASS,ZHOUCI,JIECI) values ('%s','%s','%s','%s')"  % (a,b,c,d))
    conn.commit()
    #关闭数据库连接
    conn.close()

#查询数据
def select():
    conn = sqlite3.connect("build.db")
    cursor = conn.cursor()
    cursor.execute('select * from CNAME ')
    values = cursor.fetchall()
    cursor.close()
    conn.close()
    return values

#每节课截取处理函数
def lesson(a):
    str = re.split('-|\[', a)
    return str[1]

# 选择函数
# noinspection PyInterpreter
def show(args):
    A11=[]
    a11=[]
    a111=[]
    for i in xrange(len(args)):
        t=args[i][0:10]
        s=args[i][10:len(args[i])][:-1]
        n = re.split(u'-|,',s)
        if t not in A11:
            A11.append(t)
            a11.append(s)
            a111.append(args[i])
        else:
            k=A11.index(t)
            m= re.split(u'-|,',a11[k])
            if m[-1] <= n[0] or m[0]<=n[-1]:
                a11[k] = a11[k]+','+s
                a111[k] = A11[k]+a11[k]+'\n'
            elif m[0] >= n[-1] or m[-1]<=n[0]:
                a11[k] = s+','+a11[k]
                a111[k] = A11[k]+a11[k]+'\n'
    return a111

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