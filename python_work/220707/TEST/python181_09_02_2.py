'''
문제2
다음 튜플을 만들어보자. 이 튜플은 1부터 시작해서 100까지 증가한다.
그리고 다시 1씩 줄어들어서 마지막에 1로 끝난다.
    (1, 2, 3 ... 98 ,99, 100, 99, 98 ... 3, 2, 1)
물론 위의 숫자를 모두 입력해서 만들라는 뜻이 아니다.
레인지와 이를 튜플로 바꿔주는 함수를 사용해서 한 줄에 입력 가능한
수준으로 만들어보라는 의미이다.
참고로 이러한 튜플을 만들려면 값이 증가하는 튜플과 감소하는 튜플을 각각 생성해서
이를 하나로 묶는 과정을 거쳐야 한다.
'''


# tp = tuple(range(1, 100)) + tuple(range(100, 0, -1))
# print(tp)

# a = [i for i in range(1, 101)]
# a = tuple(a)
# b = [i for i in range(99, 0, -1)]
# b = tuple(b)
# c = a + b
# print(c)

import numpy as np

a = np.arange(1, 10)
print(list[a])

a = [i for i in range(1, 10)]
print(a)
