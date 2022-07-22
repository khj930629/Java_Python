import sys


def doA():
    for i in [10, 20, 30, 40, 50, 60, 70, 80, 100, 110, 120, 130, 140]:
        yield i


a = [10, 20, 30, 40, 50, 60, 70, 80, 100, 110, 120, 130, 140]
b = doA()

print(sys.getsizeof(a))
print(sys.getsizeof(b))

print(next(b))
print(next(b))
print(next(b))
