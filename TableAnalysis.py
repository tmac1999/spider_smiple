#!/usr/bin/python
# -*- coding:utf8 -*- 为了支持中文注释
import sqlite3

if __name__ == '__main__':
    connect = sqlite3.connect('/Users/lianhua/Downloads/MM.sqlite')
    cursor = connect.cursor()
    cursor.execute("select name from sqlite_master where type='table' order by name;")
    # cursor.execute("select * from sqlite_master where name='tablename' and sql like '%fieldname%'; ")
    # cursor.execute("select count(rownum) from [table]")
    # cursor.fetchall()

    #
    for row in cursor:
        # print row[0]
        cursorTemp = connect.cursor()
        # cursorRowCount.execute("select * from sqlite_master where name='"+row[0]+"' and sql like 'Des'; ")
        # cursorRowCount.execute("select count(*) from " + row[0])
        cursorTemp.execute("PRAGMA table_info(["+row[0] +"])")
        fetchall = cursorTemp.fetchall()
        if fetchall[-1].__contains__('Des') :
            cursorMyMsgRowCount = connect.cursor()
            cursorOtherMsgRowCount = connect.cursor()
            cursorMyMsgRowCount.execute("select count(*) from " + row[0]+" where Des = 0")
            cursorOtherMsgRowCount.execute("select count(*) from "+row[0])
            msg_row_count_next_ = cursorMyMsgRowCount.next()[0]
            next_ = cursorOtherMsgRowCount.next()[0]
            # cursorRowCount.next() 返回第一行数据，tuple类型，第0号位置即Des=0的行数（自己说话的行数）
            print row[0], ":", msg_row_count_next_, '-', next_, '-',msg_row_count_next_/float(next_)#分母应该还要减去Type=10000 的msg，因为这类msg都Des=1

