import sqlite3

if __name__ == '__main__':
    connect = sqlite3.connect('/Users/lianhua/Downloads/MM(1).sqlite')
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
        if cursorTemp.fetchall()[-1].__contains__('Des') :
            print row[0], ":", cursorTemp.fetchall()

