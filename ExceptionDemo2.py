# User Define Exceptions

class MyError(Exception):
    pass

try:
    raise MyError('some error')
except MyError as e:
    print(e)
