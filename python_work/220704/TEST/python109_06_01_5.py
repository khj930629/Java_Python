'''
문제5
빈 리스트를 만들어서 그 안에 1부터 10까지 넣었다가,
다시 10부터 1까지 꺼내는(삭제하는) 코드를 만들어보자.
이번에도 문제 4와 마찬가지로 for 루프를 이용하자.
'''
st = []
for i in range(10):
    st.append(i+1)
    print(st)

for i in range(10):
    st.pop(-1)
    print(st)
