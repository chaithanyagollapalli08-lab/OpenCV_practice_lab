import numpy as np
import cv2
import matplotlib.pyplot as plt
img=cv2.imread('images/lena_color_256.tif')
im=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.imshow(im)
plt.axis('off')
plt.show()
