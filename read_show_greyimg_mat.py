import numpy as np
import matplotlib.pyplot as plt

lena_img=plt.imread('images/lena_gray_256.tif')

print(lena_img.shape)
print(lena_img.size)
plt.imshow(lena_img,cmap='gray')
plt.show()

