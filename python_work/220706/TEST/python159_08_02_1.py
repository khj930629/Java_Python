'''
문제1
6과 45의 최소공배수를 구하는 코드를 while 루프 기반으로 작성해보자.
참고로 6으로도 나눠지고 45로도 나눠지는 값들 중에서 제일 작은 값이 '최소공배수'이다. 
따라서 45부터 시작해서 값을 1씩 증가시켜가면서 
6과 45로 나누어 떨어지는 첫 번째 값을 찾으면 된다. 
코드는 다음과 같이 작성하자.
    lcm = 0     # 변수 lcm을 선언하고, 그리고 필요하면 변수를 추가로 선언하고
                # 변수 lcm에 최소공배수를 찾아서 저장하는 코드를 구성하고
....
    lcm         # 변수 lcm에 저장된 값을 출력한다. (90이 출력되어야 정답이다.)
'''
lcm = 0
n = 45
while True:
    if (n % 6 == 0) and (n % 45 == 0):
        lcm = n
        break
    n = n + 1
print("lcm", lcm)
    