import numpy as np

data = np.load('BIGDATA_IMAGE_WORK/20220809/carprice.npz',
               allow_pickle=True)

x_data = data['x_data']
y_data = data['y_data']

print(x_data.shape)
print(y_data.shape)

print(x_data[:5])
print(y_data[:5])
