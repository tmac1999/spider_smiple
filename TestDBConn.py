import MySQLdb

connect = MySQLdb.connect(host='127.0.0.1',
                          port=3306, user='root',
                          passwd='123456', db='github', charset='utf8')

cursor = connect.cursor()

print cursor
print connect
cursor.close()
connect.close()