class ChatTable(object):

    def __str__(self):
        return self.tableName

    def __init__(self, tableName, myMsgCount, totalMsgCount, percentage):
        self.tableName = tableName
        self.myMsgCount = myMsgCount
        self.otherMsgCount = totalMsgCount
        self.percentage = percentage

    def __cmp__(self, other):
        if self.myMsgCount < other.myMsgCount:
            return 1
        elif self.myMsgCount > other.myMsgCount:
            return -1
        else:
            return 0

    def __dict__(self):
        return self.tableName

    def dic(self):
        return self.tableName+':', self.myMsgCount, '-', self.otherMsgCount, '-', self.percentage