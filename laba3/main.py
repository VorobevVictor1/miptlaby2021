import numpy as np
import matplotlib.pyplot as plt
import mpmath as mp
from PIL import Image

color_arr = np.zeros((100, 100, 4), dtype=np.uint8)
x_arr = np.linspace(-2., 2., 100, dtype=np.float64)
y_arr = np.linspace(-2., 2., 100, dtype=np.float64)
n_arr = np.zeros((100, 100), dtype=int)

for i in range(x_arr.shape[0]):
    for j in range(y_arr.shape[0]):
        z_x = 0
        c_x = x_arr[i]
        z_y = 0
        c_y = y_arr[j]

        for it in range(100):
            z_x_new = z_x ** 2 - z_y ** 2 + c_x
            z_y_new = 2 * z_x * z_y + c_y
            z_x = z_x_new
            z_y = z_y_new
            if z_x ** 2 + z_y ** 2 > 4:
                break
        n_arr[i, j] = it
        color_arr[i, j] = (it % 255, it % 127, it % 63, 255)
plt.imshow(n_arr, cmap='flag')
im = Image.fromarray(color_arr)
plt.colorbar()
plt.imshow(im)