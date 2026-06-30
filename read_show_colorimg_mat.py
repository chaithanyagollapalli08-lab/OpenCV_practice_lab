import numpy as np
import matplotlib.pyplot as plt

color_img=plt.imread('images/lena_color_256.tif')

print(color_img.shape)
print(color_img.size)
plt.imshow(color_img)
plt.show()
