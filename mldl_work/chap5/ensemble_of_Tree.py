# %%
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate, train_test_split

print("-" * 20 + " < 데이터 수집 > " + "-" * 20)
data = pd.read_csv('./wine.csv')
print(data.head())
print(data.describe())

print("-" * 20 + " < 데이터 전처리 > " + "-" * 20)
wine_data = data[['alcohol', 'sugar', 'pH']].to_numpy()
wine_class = data['class'].to_numpy()

print("-" * 20 + " < 학습과 테스트 데이터셋 분할 > " + "-" * 20)
train_input, test_input, train_target, test_target = \
    train_test_split(wine_data, wine_class, test_size=0.2, random_state=42)

print(train_input.shape)

rf = RandomForestClassifier(n_jobs=-1, random_state=42)
scores = cross_validate(rf, train_input, train_target,
                        return_train_score=True, n_jobs=-1)

print(np.mean(scores['train_score']), np.mean(scores['test_score']))

rf.fit(train_input, train_target)
print(rf.feature_importances_)

rf = RandomForestClassifier(oob_score=True, n_jobs=-1, random_state=42)

rf.fit(train_input, train_target)
print(rf.oob_score_)
# %%
