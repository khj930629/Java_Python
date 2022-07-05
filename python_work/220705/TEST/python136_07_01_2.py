'''
문제2
파이썬에서는 다음과 같이 문장을 작성하는 것이 가능하다.
    num = 3
    1 < num < 5     # num의 값은 1보다 크고 5보다 작은가?
    True
그런데 이는 파이썬이기에 지원되는 방식이다. 다른 코딩 언어들은 다음과 같은 연산을 지원하지만,
    1 < num     # num은 1보다 큰가?
    True
    num < 5     # num은 5보다 작은가?
    True
다음과 같은 연산은 지원하지 않는 경우가 있다.
    1 < num < 5     #파이썬이라 가능한 연산
자! 그럼 파이썬도 위와 같이 문장을 구성할 수 없다고 가정하고, 
num에 저장된 값이 '1보다 크면서 동시에 5보다 작은가?'를 묻는 문장을 만들어서
다음 빈 공간을 채워보자.
    num = 3
    _______
    True
'''
num = 3
1 < num and num < 5
True
