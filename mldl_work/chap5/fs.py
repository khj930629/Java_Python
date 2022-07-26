# %%
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
import seaborn as sns

print("-" * 20 + " < 데이터 로드 > " + "-" * 20)
train_df = pd.read_excel('./mldl_work/chap5/fs.xlsx', sheet_name='train')
test_df = pd.read_excel('./mldl_work/chap5/fs.xlsx', sheet_name='test')

print("-" * 20 + " < 데이터 분석 > " + "-" * 20)
print(train_df.head())
print(test_df.head())

print("-" * 20 + " < 데이터 전처리 > " + "-" * 20)
train_input = train_df[['Father']].to_numpy()
train_target = train_df['Son'].to_numpy()

test_input = test_df[['Father']].to_numpy()
test_target = test_df['Son'].to_numpy()

print("-" * 20 + " < 선형회귀 모델 학습 > " + "-" * 20)
lr = LinearRegression()
lr.fit(train_input, train_target)


print("-" * 20 + " < 선형회귀 모델 검증 > " + "-" * 20)
학습점수 = lr.score(train_input, train_target)
테스트점수 = lr.score(test_input, test_target)

print(학습점수)
print(테스트점수)

print("-" * 20 + " < 선형회귀 모델 예측 > " + "-" * 20)
pred = lr.predict([[160]])
print('예측키 = ', pred)

print("-" * 20 + " < 랜덤포레스트 모델 학습 > " + "-" * 20)
lr = RandomForestRegressor()
lr.fit(train_input, train_target)

print("-" * 20 + " < 랜덤포레스트 모델 검증 > " + "-" * 20)
학습점수 = lr.score(train_input, train_target)
테스트점수 = lr.score(test_input, test_target)

print(학습점수)
print(테스트점수)

print("-" * 20 + " < 랜덤포레스트 모델 예측 > " + "-" * 20)
pred = lr.predict([[160]])
print('예측키 = ', pred)

prediction = lr.predict(train_input[:30])

plt.scatter(train_input, train_target)
plt.plot(train_input[:30], prediction, c='#ff0000')
plt.xlabel('father')
plt.ylabel('son')
plt.show
# %%
