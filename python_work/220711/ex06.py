cnt = 100
i = 100


def doA():
    cnt = 0
    print('지역변수', cnt)


doA()
print('전역변수', cnt)


def doB():
    for i in range(10):
        print('result = ', i)


doB()
print(i)
