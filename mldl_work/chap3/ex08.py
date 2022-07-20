# %%
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from scipy.special import expit
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('https://bit.ly/fish_csv_data')
data.to_csv('fish_data.csv')

print(data.head())

fish_input = data[['Weight', 'Length',
                   'Diagonal', 'Height', 'Width']].to_numpy()
print(fish_input[:5])

fish_target = data['Species'].to_numpy()
print(fish_target[:5])

train_input, test_input, train_target, test_target = \
    train_test_split(fish_input, fish_target, random_state=42)

ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

print(train_scaled[:5])
print(train_target[:5])
print(test_scaled[:5])
print(test_target[:5])

kn = KNeighborsClassifier(n_neighbors=3)
kn.fit(train_scaled, train_target)

예측값 = kn.predict(test_scaled)
print(예측값[:5])
print(test_target[:5])

pre = [242., 25.4, 30., 11.52, 4.02]
pre_scaled = ss.transform([pre])

print(pre_scaled)
pre_value = kn.predict(pre_scaled)
print(pre_value)

score = kn.score(test_scaled, test_target)
print(score)

'''
로지스틱 회귀
이름은 회귀이지만 분류 모델이다. 이 알고리즘은 선형 회귀와 동일하게
선형 방정식을 학습한다.
z = a * (weight) + b * (length) + c * (diagonal) + 
d * (height) + e * (width) + f

z가 아주 큰 음수일 때 0이 되고, z가 아주 큰 양수일 때 1이 되도록 바꾸는 방법?
시그모이드 함수(로지스틱 함수)를 사용하면 가능
'''
z = np.arange(-5, 5, 0.1)
phi = 1 / (1+np.exp(-z))
print(z)
print(phi)

plt.plot(z, phi)
plt.xlabel('z')
plt.ylabel('phi')
plt.show()

# 로지스틱 회귀로 이진 분류 수행하기
indexs = (train_target == 'Bream') | (train_target == 'Smelt')
도미빙어데이터 = train_scaled[indexs]
도미빙어타겟 = train_target[indexs]

print(도미빙어데이터.shape)
print(도미빙어타겟.shape)

lr = LogisticRegression()
lr.fit(도미빙어데이터, 도미빙어타겟)

indexs = (test_target == 'Bream') | (test_target == 'Smelt')
도미빙어데이터 = test_scaled[indexs]
도미빙어타겟 = test_target[indexs]

score = lr.score(도미빙어데이터, 도미빙어타겟)
print(score)

pre = [242., 25.4, 30., 11.52, 4.02]
pre_scaled = ss.transform([pre])

pre_value = lr.predict(pre_scaled)
print(pre_value)

z = lr.decision_function(도미빙어데이터)
print(z)

# 시그모이드 함수
'''
phi = 1/(1+np.exp(-z))
print(phi)
'''
phi = expit(z)
print(phi)

# 로지스틱 회귀로 다중 분류 수행하기

훈련데이터점수리스트 = []
테스트데이터점수리스트 = []

for i in range(1, 100):
    lr = LogisticRegression(C=i, max_iter=1000)
    lr.fit(train_scaled, train_target)

    훈련데이터점수 = lr.score(train_scaled, train_target)
    테스트데이터점수 = lr.score(test_scaled, test_target)

    훈련데이터점수리스트.append(훈련데이터점수)
    테스트데이터점수리스트.append(테스트데이터점수)

print(훈련데이터점수)
print(테스트데이터점수)
print(np.argmax(훈련데이터점수리스트))
print(np.argmax(테스트데이터점수리스트))

plt.plot(range(1, 100), 훈련데이터점수리스트)
plt.plot(range(1, 100), 테스트데이터점수리스트)
plt.show()

# Whitefish,
pre = [[242., 25.4, 30., 11.52, 4.02], [363., 29., 33.5,
                                        12.73, 4.4555], [1000, 40, 43.5, 12.354, 6.525]]
pre_scaled = ss.transform(pre)

pre_value = lr.predict(pre_scaled)
print(pre_value)

lgb = RandomForestClassifier()
lgb.fit(train_scaled, train_target)

훈련데이터점수 = lgb.score(train_scaled, train_target)
테스트데이터점수 = lgb.score(test_scaled, test_target)

print(훈련데이터점수)
print(테스트데이터점수)

pre = [[242., 25.4, 30., 11.52, 4.02],
       [363., 29., 33.5, 12.73, 4.4555],
       [1000, 40, 43.5, 12.354, 6.525]]
pre_scaled = ss.transform(pre)

pre_value = lgb.predict(pre_scaled)
print(pre_value)
# %%
