'''
문제2
위의 문제 1에서는 리스트에 다음 순서대로 값을 저장하고 꺼냈다.
    저장 순서 1, 2, 3
    꺼낸 순서 1, 2, 3
이번에는 다음 순서대로 값을 저장하고 꺼내도록 코드를 작성해보자.
    저장 순서 1, 2, 3
    꺼낸 순서 3, 2, 1
즉, 문제 1에서와 달리 값을 뒤에서부터 꺼내는 코드를 작성하라는 뜻이다.
조금 힌트를 주자면, pop 함수에 전달하는 인덱스 값은 음수도 가능하다.
'''
st = []
st.append(1)
st.append(2)
st.append(3)
print(st)
st.pop(-1)
print(st)
st.pop(-1)
print(st)
st.pop(-1)
print(st)