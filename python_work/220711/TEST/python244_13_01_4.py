'''
문제4
리스트에 담긴 객체들 중에서 '장지우'의 전화번호를 
다음과 같이 수정하는 코드를 for 루프를 기반으로 작성해보자
    장지우  010-999-999
그리고 수정이 끝나면 정상적으로 수정되었는지 확인하기 위해서 
'장지우'의 정보를 찾아서 출력하는 for 루프를 작성해보자.
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

for i in fs:
    if i.get_name() == '장지우':
        i.set_phone('010-999-999')

for i in fs:
    if i.get_name() == '장지우':
        i.show_info()
