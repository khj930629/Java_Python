'''
문제1
다음은 빈 리스트를 만들어서 그 안에 1, 2, 3을 넣었다가 넣은 순서대로 꺼내는
코드의 실행 흐름이다.
    st = [] # 빈 리스트 생성
            # 리스트에 1 추가
            # 리스트에 2 추가
            # 리스트에 3 추가
    st
[1,2,3]
            # 리스트에서 1 삭제
1
            # 리스트에서 2 삭제
2
            # 리스트에서 3 삭제
3
    st
[]
위의 실행 흐름이 완성되도록 빈칸에 문장들을 채워 넣자.
'''
st = []
st.append(1)
st.append(2)
st.append(3)
print(st)
st.pop(0)
print(st)
st.pop(0)
print(st)
st.pop(0)
print(st)
