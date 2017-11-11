from Friend import Friend
from FriendAnalysis import FriendAnalysis

if __name__ == '__main__':
    # friend_analysis = FriendAnalysis()
    # dbLocation = '/Users/lianhua/Downloads/WCDB_Contact.sqlite'
    # nameDict = friend_analysis.openDB(dbLocation)
    friend = Friend('asd', 'asddasda')
    d = {}
    d['aaa'] = friend
    get = d.get('aaa')
    print get.contactRemark, get.userName