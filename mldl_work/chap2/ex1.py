from operator import index
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# 데이터전처리
data = pd.read_excel('data.xlsx')
print(data)

length = data['length'].to_numpy()
print(length[:5])
weight = data['weight'].to_numpy()
print(weight[:5])

data = np.column_stack((length, weight))
print(data[:5])
print(data.shape)

fish_target = np.concatenate((np.ones(35), np.zeros(14)))
print(fish_target)

# 훈련세트와 테스트 세트 나누기(사이킷런)
train_input, test_input, train_target, test_target = train_test_split(
    data, fish_target, random_state=42, stratify=fish_target)
print(train_input.shape)
print(test_input.shape)

print(train_target.shape)
print(test_target.shape)

# 수상한 도미 한마리
kn = KNeighborsClassifier()
# 학습해라 train_input이 들어가면 train_target이 나온다는 걸로..
kn.fit(train_input, train_target)
# 점수보자 test_input이 들어가면 test_target이 나오는데 너가 예측한 거랑 동일하냐?
score = kn.score(test_input, test_target)
print(score)

prevalue = kn.predict([[25, 150]])
print(prevalue)

dis, index = kn.kneighbors([[25, 150]])
print(dis)
print(index)
print(train_input[index])

# plt.scatter(train_input[:, 0], train_input[:, 1])
# plt.scatter(test_input[:, 0], test_input[:, 1])
# plt.scatter(train_input[index, 0], train_input[index, 1], marker='D')
# plt.legend(['train', 'test', 'neighbors'])
# plt.scatter(25, 150, marker='^')

# plt.show()

# 기준을 잡아라
mean = np.mean(train_input, axis=0)
std = np.std(train_input, axis=0)

print(mean, std)

train_scaled = (train_input-mean)/std
test_scaled = (test_input-mean)/std

predata = (np.array([25, 150])-mean)/std
print(predata)

plt.scatter(train_scaled[:, 0], train_scaled[:, 1])
plt.scatter(predata[0], predata[1])
plt.show()

# 전처리 데이터로 모델 훈련하기
kn = KNeighborsClassifier()
kn.fit(train_scaled, train_target)

score = kn.score(test_scaled, test_target)
print(score)

predictvalue = kn.predict([predata])
print(predictvalue)

dis, index = kn.kneighbors([predata])

plt.scatter(train_scaled[:, 0], train_scaled[:, 1])
plt.scatter(predata[0], predata[1], marker='^')
plt.scatter(train_scaled[index, 0], train_scaled[index, 1], marker='D')
plt.show()
