'''
캘리포니아 주택 가격 데이터셋
'''
# %%
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.preprocessing import PolynomialFeatures

print("-" * 20 + " < 데이터 수집 > " + "-" * 20)
dataset = datasets.fetch_california_housing()

x = dataset.data
y = dataset.target

print(x)
print(y)

print("-" * 20 + " < 데이터 분석 > " + "-" * 20)
dataframe = pd.DataFrame(x, columns=dataset.feature_names)
print(dataframe.head())
print(dataframe.tail())

print("-" * 20 + " < 학습과 테스트 데이터셋 분할 > " + "-" * 20)
train_input, test_input, train_target, test_target = \
    train_test_split(x,y,random_state=42)

print("-" * 20 + " < 선형회귀 모델 학습 > " + "-" * 20)
lr = LinearRegression()
lr.fit(train_input,train_target)

print("-" * 20 + " < 선형회귀 모델 검증 > " + "-" * 20)
학습점수 = lr.score(train_input,train_target)
테스트점수 = lr.score(test_input,test_target)

print(f'학습점수 = {학습점수}')
print(f'테스트점수 = {테스트점수}')

print("-" * 20 + " < 선형회귀 모델 예측 > " + "-" * 20)
# print(train_input[:2])
# print(np.round(train_input[:2]))
# print(train_target[:2])
'''
[[   4.2143       37.            5.28823529    0.97352941  860.
     2.52941176   33.81       -118.12      ]
 [   5.3468       42.            6.36432161    1.0879397   957.
     2.40452261   37.16       -121.98      ]]
[2.285 2.799]
'''

pred = lr.predict(train_input[:2])
print(pred)
pred = lr.predict(np.round(train_input[:2]))
print(pred)

print("-" * 20 + " < 다항회귀 모델 학습 > " + "-" * 20)
poly = PolynomialFeatures(degree=4)
poly.fit(train_input)

train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

print(train_poly.shape)
print(test_poly.shape)

lr.fit(train_poly, train_target)

print("-" * 20 + " < 다항회귀 모델 검증 > " + "-" * 20)
학습점수 = lr.score(train_poly,train_target)
테스트점수 = lr.score(test_poly,test_target)

print(f'학습점수 = {학습점수}')
print(f'테스트점수 = {테스트점수}')

print("-" * 20 + " < 다항회귀 모델 예측 > " + "-" * 20)
'''
[2.285 2.799]
'''
pred = lr.predict(train_poly[:2])
print(pred)
pred = lr.predict(np.round(train_poly[:2]))
print(pred)

print("-" * 20 + " < Ridge 규제 > " + "-" * 20)
ridge = Ridge()
ridge.fit(train_poly,train_target)

print("-" * 20 + " < Ridge 검증 > " + "-" * 20)
학습점수 = ridge.score(train_poly,train_target)
테스트점수 = ridge.score(test_poly,test_target)

print(f'학습점수 = {학습점수}')
print(f'테스트점수 = {테스트점수}')

print("-" * 20 + " < Ridge 예측 > " + "-" * 20)
pred = ridge.predict(train_poly[:2])
print(pred)
pred = ridge.predict(np.round(train_poly[:2]))
print(pred)

print("-" * 20 + " < Lasso 규제 > " + "-" * 20)
lasso = Lasso()
lasso.fit(train_poly,train_target)

print("-" * 20 + " < Lasso 검증 > " + "-" * 20)
학습점수 = lasso.score(train_poly,train_target)
테스트점수 = lasso.score(test_poly,test_target)

print(f'학습점수 = {학습점수}')
print(f'테스트점수 = {테스트점수}')

print("-" * 20 + " < Lasso 예측 > " + "-" * 20)
pred = lasso.predict(train_poly[:2])
print(pred)
pred = lasso.predict(np.round(train_poly[:2]))
print(pred)
# %%
