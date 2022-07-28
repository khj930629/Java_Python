# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from fruitslog import getlog

a = cv2.imread('a.jpg', cv2.IMREAD_GRAYSCALE)
print(a.shape)

# plt.imshow(a, cmap='gray_r')
# plt.show()

lr = getlog()
pred = lr.predict(a.reshape(-1, 10000))
print(pred)
# %%
