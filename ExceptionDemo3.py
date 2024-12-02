# if you wants to string as a exception

class MyError(Exception):
    def __init__(self,msg):
        self.msg=msg

    def __str__(self):
        return 'creating my exception'

try :
    raise MyError('some error')
except MyError as e:
    print(e)
