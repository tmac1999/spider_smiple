import sqlite3


class FriendAnalysis(object):
    def openDB(self,DBLocation):
        connect = sqlite3.connect(DBLocation)
        cursor = connect.cursor()
        execute = cursor.execute('select userName from Friend')
        for row in execute:
            print row[0]

