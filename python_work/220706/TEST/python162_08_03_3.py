'''
문제3
문제 2의 결과에서 continue를 사용하지 않았다면 
이번에는 continue를 사용하는 방식으로 코드를 수정해보자.
반대로 문제 2에서 continue를 사용했다면
이번에는 continue를 사용하지 않는 방식으로 코드를 수정해보자.
'''
n = 1
while n < 100:
    n += 1
    if (n % 2 == 0) or (n % 3 == 0):
        continue
    print(n, end=' ')
