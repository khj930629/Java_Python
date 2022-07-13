'''
문제3
리스트에 담긴 객체 중에서 성이 '윤'인 사람의 이름과 전화번호를 전부 출력하는 for 루프를 작성해보자.
참고로 이 문제의 해결을 위해서는 다음 함수를 사용할 필요가 있다.
(이 함수는 7장에서 소개한 함수이다.)
    s.startswith(prefix)        문자열 s가 prefix로 시작하면 True, 아니면 False 반환
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

fs = []
fs.append(Friend("윤지민", '010-111-222'))
fs.append(Friend("이선준", '010-333-444'))
fs.append(Friend("장지우", '010-555-666'))
fs.append(Friend("윤지율", '010-777-888'))

for i in fs:
    i.show_info()

for i in fs:
    if i.get_name().startswith('윤'):
        i.show_info()
