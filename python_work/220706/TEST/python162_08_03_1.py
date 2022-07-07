'''
문제1
다음은 구구단 중에서 7단을 출력하는 예제이다.
    for i in range(1,10):
        print(7 * i, end = ' ')
    7 14 21 28 35 42 49 56 63
    
위의 예제에 continue 관련 코드를 넣어서 결과가 짝수인 경우에만 출력되도록 해보자.
즉 7은 출력되지 않고 14는 출력되어야 한다.
'''
for i in range(1, 10):
    if (7 * i) % 2:
        continue
    print(7 * i, end=' ')
