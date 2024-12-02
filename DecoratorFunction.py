def decorator(fun):

    def wrapper(msg):
        print('*' * 10)
        fun(msg)
        print('*' * 10)
    return wrapper

# @decorator
def display(msg):
    print(msg)

# if we don't pass decorator as object than cmmt-out that @decorator
# and remove belows 1st line.
d=decorator(display)
d('vanakkam')

