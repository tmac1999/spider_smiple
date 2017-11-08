import sqlite3

if __name__ == '__main__':
    connect = sqlite3.connect('/Users/lianhua/Downloads/MM(1).sqlite')
    cursor = connect.cursor()
    cursor.execute("select name from sqlite_master where type='table' order by name;")
    # cursor.execute("select count(rownum) from [table]")
    # cursor.fetchall()
    # todo 1建立每个对话表与人名的对应关系 2群聊中人名与id对应 3按聊天消息条数排序，发出与接收百分比 4 群聊中被@ 分析 5饼状图 和 条形图
    #
    for row in cursor:
        # print row[0]
        cursorRowCount = connect.cursor()
        cursorRowCount.execute("select count(*) from " + row[0])
        print row[0], ":", cursorRowCount.fetchall()
