'''
문제2
문제1에서 정의한 클래스 Friend를 기반으로 다음 네 친구의 정보를 담은
Friend 객체를 각각 생성해서 리스트에 담아보자.
그리고 이 리스트는 지우지 말자.
문제 3, 4에서 이 리스트를 대상으로 문제를 제시한다.
    윤지민      010-111-222
    이선준      010-333-444
    장지우      010-555-666
    윤지율      010-777-888
그리고 이어서 리스트에 담긴 객체가 지니는 이름과 전화번호를 모두 출력하는
for 루프를 작성해보자.
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


# f = Friend('윤성우', '010-1111-222')
# f.get_name()
# f.get_phone()
# f.set_phone('010-333,444')
# f.show_info()

fs = []
fs.append(Friend("윤지민", '010-111-222'))
fs.append(Friend("이선준", '010-333-444'))
fs.append(Friend("장지우", '010-555-666'))
fs.append(Friend("윤지율", '010-777-888'))

for i in fs:
    i.show_info()
