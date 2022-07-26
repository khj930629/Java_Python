# %%
import cv2
from matplotlib import rc
import numpy as np
import matplotlib.pyplot as plt

rc('font', family="AppleGothic")

woyo = cv2.imread('woyo.png')
print(woyo.shape)
pltwoyo = cv2.cvtColor(woyo, cv2.COLOR_BGR2RGB)
np.save('a.npy', pltwoyo)

plt.scatter([10, 20, 30], [10, 20, 30], s=100)
plt.text(50, 500, '내 이름은 우영우, \n거꾸로해도 똑바로 해도 우영우 \n기러기, 토마토, 스위스, 인도인, \n별똥별, 역삼역...(?!)', c='white')
plt.axis('off')
plt.imshow(pltwoyo)
plt.show
# %%
