'''
튜플을 인자로 전달하면, 이를 리스트로 바꿔주는 함수를 만들어보자.
예를 들어서 to_list라는 이름으로 함수를 만들었다면 다음과 같이 작동해야한다.
    ds = (1,2,3)        # 튜플이다!
    ds = to_list(ds)    # 튜플을 줄게 리스트 다오
    ds
    [1,2,3]
만약에 함수를 제대로 만들었다면, 다음과 같이 이 함수는 문자열을 대상으로도 잘 작동할 것이다.
    ds = "hello"        # 문자열이다!
    ds = to_list(ds)    # 문자열 줄게 리스트 다오
    ds
    ['h','e','l','l','o']
'''


def to_list(t):
    st = []
    for i in t:
        st.append(i)
    return st


ds = (1, 2, 3)
ds = to_list(ds)
print(ds)

ds = "hello"
ds = to_list(ds)
print(ds)
