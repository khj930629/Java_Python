# %%
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
import matplotlib.pyplot as plt

print("#" * 20 + " < 데이터 수집하기 > " + "#" * 20)
data = pd.read_csv('fish_data.csv')
print(data.info())

print("#" * 20 + " < 데이터 전처리하기 > " + "#" * 20)
fish_input = data[['Weight', 'Length',
                   'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = data['Species'].to_numpy()
print(fish_input.shape)
print(fish_target.shape)

print(fish_input[:5])
print(fish_target[:5])

print("#" * 20 + " < 훈련과 테스트 데이터셋 분할하기 > " + "#" * 20)
train_input, test_input, train_target, test_target = \
    train_test_split(fish_input, fish_target, random_state=42)

print(train_input[:5])
print(train_target[:5])

print("#" * 20 + " < 표준화로 데이터 분류하기 > " + "#" * 20)
ss = StandardScaler()
ss.fit(train_input)

train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

print(train_scaled[:5])
print(train_target[:5])

print("#" * 20 + " < 확률적경사하강법 시행하기 > " + "#" * 20)
sgd = SGDClassifier(loss='log', max_iter=100, random_state=42)
sgd.fit(train_scaled, train_target)

훈련점수 = sgd.score(train_scaled, train_target)
테스트점수 = sgd.score(test_scaled, test_target)

print(훈련점수)
print(테스트점수)

예측값 = sgd.predict(test_scaled[:5])
print(예측값)
print(test_target[:5])

print("#" * 20 + " < 점진적인 학습하기 > " + "#" * 20)
sgd.partial_fit(train_scaled, train_target)

훈련점수 = sgd.score(train_scaled, train_target)
테스트점수 = sgd.score(test_scaled, test_target)

print(훈련점수)
print(테스트점수)

예측값 = sgd.predict(test_scaled[:5])
print(예측값)
print(test_target[:5])

sgd.partial_fit(train_scaled, train_target)

훈련점수 = sgd.score(train_scaled, train_target)
테스트점수 = sgd.score(test_scaled, test_target)

print(훈련점수)
print(테스트점수)

예측값 = sgd.predict(test_scaled[:5])
print(예측값)
print(test_target[:5])

print("#" * 20 + " < Whitefish 찾기 > " + "#" * 20)
indexsx = (train_target == 'Whitefish')
예측값 = sgd.predict(train_scaled[indexsx])
print(예측값)
print(train_target[indexsx])

print("#" * 20 + " < 에포크와 과대/과소적합 > " + "#" * 20)
sc = SGDClassifier(loss='log', random_state=42)

train_score = []
test_score = []

classes = np.unique(train_target)

for _ in range(300):
    sc.partial_fit(train_scaled, train_target, classes=classes)

    train_score.append(sc.score(train_scaled, train_target))
    test_score.append(sc.score(test_scaled, test_target))

print(train_score[:5])
print(test_score[:5])

print("#" * 20 + " < 데이터 시각화하기 > " + "#" * 20)
plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()

print(test_score)
# %%
