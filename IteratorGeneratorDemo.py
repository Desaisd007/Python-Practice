


def days():
    day=['sun','mon','tues','wed','thurs','fri','sat']
    i=0

    while True:
        x = day[i]
        i=(i+1)%7
        yield x

d=days()
print(next(d))


