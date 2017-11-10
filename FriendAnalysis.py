#!/usr/bin/python
# -*- coding:utf8 -*- 为了支持中文注释
import hashlib
import sqlite3


class FriendAnalysis(object):
    # 返回MD5-UerName键值对
    def openDB(self,DBLocation):
        connect = sqlite3.connect(DBLocation)
        cursor = connect.cursor()
        execute = cursor.execute('select userName from Friend')
        nameDict = {}
        for row in execute:
            md5 = hashlib.md5(row[0]).hexdigest()

            print md5,':',row[0]
            nameDict[md5] = row[0]
            # print row[0]
        return nameDict
