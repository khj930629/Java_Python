'''
문제2
인자로 전달된 리스트에 저장되어 있는 모든 값들을 역순으로 출력하는 함수를 만들어보자.
예를 들어서 함수의 이름이 show_reverse라고 하면, 다음과 같은 실행 결과를 보여야 한다.
    show_reverse([1,2,3,4,5])
    5 4 3 2 1
함수를 잘 만들었다면 다음과 같이 문자열을 대상으로도 동작을 하니, 다음과 같이 문자열을
대상으로도 동작하는지 확인해보기 바란다.
    show_reverse("ABCDEFG)
    G F E D C B A
'''


def show_reverse(st):
    for i in range(len(st)):
        print(st[(i+1)*-1], end=' ')


show_reverse([1, 2, 3, 4, 5])
print(" ")
show_reverse("ABCDEFG")
