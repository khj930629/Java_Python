'''
문제2
우리나라의 주민등록번호는 다음과 같은 구조이다.
"070609-2011xxx"
"090716-1012xxx"
이 중에서 앞의 여섯 자리는 생년월일 정보이다. 
따라서 문자열로 표현된 위의 주민등록번호에서 생년월일 정보만 꺼내서 출력하고자 하니,
이러한 기능을 제공하는 함수를 만들어보자.
예를 들어서 함수의 이름이 birth_only라 하면 
이 함수를 대상으로 다음과 같은 결과를 보여야 한다.
    p1 = "070609-2011xxx"
    p1 = birth_only(p1)
    p1
    '070609'
    p2 = "090716-1012xxx"
    p2 = birth_only(p2)
    p2
    '090716
'''


def birth_only(pn):
    birthday = pn.split('-')
    return birthday[0]


p1 = "070609-2011xxx"
p1 = birth_only(p1)
print(p1)

p2 = "090716-1012xxx"
p2 = birth_only(p2)
print(p2)