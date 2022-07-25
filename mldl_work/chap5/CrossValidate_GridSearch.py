# %%
from scipy.stats import randint, uniform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, StratifiedKFold, cross_validate, train_test_split
from sklearn.tree import DecisionTreeClassifier

print("#" * 20 + " < 데이터 수집 > " + "#" * 20)
data = pd.read_csv('wine.csv')
print(data.head())

print("#" * 20 + " < 데이터 전처리 > " + "#" * 20)
x = data[['alcohol', 'sugar', 'pH']].to_numpy()
y = data['class'].to_numpy()
print(x)

print("#" * 20 + " < 학습과 테스트 데이터셋 분할 > " + "#" * 20)
train_input, test_input, train_target, test_target = \
    train_test_split(x, y, test_size=0.2, random_state=42)

sub_input, val_input, sub_target, val_target = \
    train_test_split(train_input, train_target, random_state=42)

print(train_input.shape)
print(sub_input.shape)
print(val_input.shape)

index0 = (val_target == 0)
print(index0)

index1 = (val_target == 1)
print(index1)

# plt.scatter(val_input[index0,1],val_input[index0,0], c="#ff0000")
# plt.scatter(val_input[index1,1],val_input[index1,0], c="#0000ff")
# plt.show()

print("#" * 20 + " < 결정 트리 > " + "#" * 20)
dt = DecisionTreeClassifier()
dt.fit(sub_input, sub_target)

학습점수 = dt.score(sub_input, sub_target)
테스트점수 = dt.score(test_input, test_target)

print(학습점수)
print(테스트점수)

''' 0 데이터 '''
pred = dt.predict([[9.4, 1.9, 3.51], val_input[10]])
print(pred)
print(val_target[10])

print(dt.feature_importances_)

plt.hist(x[:, 0], color='r')
plt.show()
plt.hist(x[:, 1], color='b')
plt.show()
plt.hist(x[:, 2], color='g')
plt.show()

print("#" * 20 + " < 교차검증 > " + "#" * 20)
scores = cross_validate(dt, train_input, train_target)
print(scores)

print(np.mean(scores['test_score']))

splitter = \
    StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)
print(scores)

print(np.mean(scores['test_score']))

print("#" * 20 + " < 하이퍼파라미터 튜닝 > " + "#" * 20)
params = {
    'min_impurity_decrease': np.arange(0.0001, 0.001, 0.0001),
    'max_depth': range(5, 20, 1),
    'min_samples_split': range(2, 100, 10)
}

gridcv = GridSearchCV(DecisionTreeClassifier(
    random_state=42), params, n_jobs=-1)
gridcv.fit(train_input, train_target)

dt = gridcv.best_estimator_  # 학습기 중 최고 성능을 나타낸 학습기를 가져와달라
print(gridcv.best_params_)

print("#" * 20 + " < 랜덤 서치 > " + "#" * 20)
rgen = randint(0, 10)
rgen.rvs(10)

np.unique(rgen.rvs(1000), return_counts=True)
plt.hist(rgen.rvs(1000))
plt.show()

ugen = uniform(0, 1)
ugen.rvs(10)

params = {'min_impurity_decrease': uniform(0.0001, 0.001),
          'max_depth': randint(20, 50),
          'min_samples_split': randint(2, 25),
          'min_samples_leaf': randint(1, 25),
          }

gs = RandomizedSearchCV(DecisionTreeClassifier(
    random_state=42), params, n_iter=100, n_jobs=-1, random_state=42)
gs.fit(train_input, train_target)

print(gs.best_params_)
print(np.max(gs.cv_results_['mean_test_score']))

dt = gs.best_estimator_

print(dt.score(test_input, test_target))
# %%
