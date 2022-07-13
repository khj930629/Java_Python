'''
문제1
친구의 이름과 전화번호 정보를 담을 수 있는 클래스를 만들어보자.
아래에서 보이는 내용과 동일한 흐름을 보이도록 클래스 Friend를 정의하면 된다.
그리고 Friend 클래스를 만들었으면 지우지 말자.
문제 2에서 이 클래스를 대상으로 문제를 제시한다.
    class Friend:
    ______________      # Friend 클래스의 정의를 여러 줄에 걸쳐 완성한다.

    f = Friend('윤성우', '010-1111-222')
    f.get_name()        # 이름 정보 반환
'윤성우'
    f.get_phone()       # 전화번호 정보 반환
'010-111-222'
    f.set_phone('010-333,444') # 전화번호 정보 수정
    f.show_info()       # 이름, 전화번호 함께 출력
이름 : 윤성우
전화번호 : 010-333-444

참고로 위와 같이 동작하게 하려면, 생성장 __init__ 함수와 다음 네 개의 함수를 만들어서 클래스 Friend를 채워야 한다.
get_name, get_phone, set_phone, show_info
'''


class Friend:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def show_info(self):
        print("이름 : ", self.name)
        print("전화번호 : ", self.phone)


f = Friend('윤성우', '010-1111-222')
f.get_name()
f.get_phone()
f.set_phone('010-333,444')
f.show_info()
