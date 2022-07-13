'''
문제2
문제 1의 결과에 이어서 모든 과자의 가격을 100원씩 올려보자.
'''
dc = {'새우깡': 700, '콘치즈': 850, '꼬깔콘 ': 750}
print(dc)

if '홈런볼' not in dc:
    dc['홈런볼'] = 900
print(dc)

for i in dc:
    dc[i] += 100
print(dc)
