'''
다음과 같이 실행되는 프로그램을 작성하시오
ex)

입력부분
a값을 입력
20
b값을 입력
30

출력부분
20+30=50
20-30=-10
20*30=600
20/30=0
'''

a = int(input("a값을 입력\n "))
b = int(input("b값을 입력\n "))

a = int(a)
b = int(b)

print(a,"+",b,"=", int(a + b))
print(a,"-",b,"=", int(a - b))
print(a,"*",b,"=", int(a * b))
print(a,"/",b,"=", int(a / b))