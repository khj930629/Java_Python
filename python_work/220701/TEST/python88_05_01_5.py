'''
88page
문제5
프롬프트 상에서 다음과 같이 리스트를 선언하고, 첫번째 값과 마지막 값을 교환하는 문장을 만들어라
st = [1,2,3,4,5]
다음과 같이 실행하면 두 변수에 값이 서로 바뀐다는 사실을 근거로 이 문제를 해결해보자.
참고로 다음과 같이 하면 두 변수에 저장된 값이 교환됨은 1장에서 소개하였다.
    x,y=2,7
    x,y=y,x
    print(x,y)
94page
문제3
다음 리스트를 대상으로 2,3,4를 삭제해보자
st=[1,2,3,4,5]
이 문제를 해결하는 방법에는 몇가지가 있는데, 여기서는 빈 리스트로 2,3,4를 대체하는 방법을 선택하자.

문제6
다음 리스트를 대상으로 짝수 번째 위치에 저장된 값들만 뽑아서 새로운 리스트를 만들어 변수 nt에
저장하는 코드를 작성해보자 그러니깐 다음 리스트를 통해서 새로 만들어야 할 리스트는 [2,4,6,8,10]이다.
st = [1,2,3,4,5,6,7,8,9,10]
'''
st = [1, 2, 3, 4, 5]
st[1:-1] = []
print(st)

st = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nt = st[1::2]
print(nt)
