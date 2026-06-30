import cv2
import numpy as np
import matplotlib.pyplot as plt
img=plt.imread('images/lena_color_256.tif')#RGB
cv2.imshow('image',img[:,:,::-1]) #BGR
cv2.waitKey()
cv2.destroyAllWindows()