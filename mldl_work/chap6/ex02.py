# %%
import numpy as np
import matplotlib.pyplot as plt

print("-" * 20 + " < 과일 사진 데이터 준비 > " + "-" * 20)
# !wget https://bit.ly/fruits_300_data -O fruits_300.npy

fruits = np.load('fruits_300.npy')
print(fruits.shape)
print(fruits[0, 0, :])

plt.imshow(fruits[0], cmap='gray')
plt.show()
plt.imshow(fruits[0], cmap='gray_r')
plt.show()

fig, axs = plt.subplots(1, 3)
axs[0].imshow(fruits[0], cmap='gray_r')
axs[1].imshow(fruits[150], cmap='gray_r')
axs[2].imshow(fruits[230], cmap='gray_r')
plt.show()

print("-" * 20 + " < 픽셀 값 분석하기 > " + "-" * 20)
apple = fruits[0:100].reshape(-1, 10000)
pineapple = fruits[100:200].reshape(-1, 10000)
banana = fruits[200:300].reshape(-1, 10000)

print(apple.shape)

print(apple.mean(axis=1))
print(pineapple.mean(axis=1))
print(banana.mean(axis=1))

plt.hist(np.mean(apple, axis=1), alpha=0.8)
plt.hist(np.mean(pineapple, axis=1), alpha=0.8)
plt.hist(np.mean(banana, axis=1), alpha=0.8)
plt.legend(['apple', 'pineapple', 'banana'])
plt.show()

apple_mean = np.mean(apple, axis=0).reshape(100, 100)
pineapple_mean = np.mean(pineapple, axis=0).reshape(100, 100)
banana_mean = np.mean(banana, axis=0).reshape(100, 100)

fig, axs = plt.subplots(1, 3, figsize=(20, 5))
axs[0].bar(range(10000), np.mean(apple, axis=0))
axs[1].bar(range(10000), np.mean(pineapple, axis=0))
axs[2].bar(range(10000), np.mean(banana, axis=0))
plt.show()

print("-" * 20 + " < 평균값과 가까운 사진 고르기 > " + "-" * 20)
abs_diff = np.abs(fruits - apple_mean)
abs_mean = np.mean(abs_diff, axis=(1, 2))
print(abs_mean.shape)

apple_index = np.argsort(abs_mean)[:100]
fig, axs = plt.subplots(10, 10, figsize=(10, 10))
for i in range(10):
    for j in range(10):
        axs[i, j].imshow(fruits[apple_index[i*10 + j]], cmap='gray_r')
        axs[i, j].axis('off')
plt.show()
# %%
