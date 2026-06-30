import cv2
import numpy as np

img=cv2.imread('images/lena_color_256.tif',1)
i=cv2.flip(img,-1)
cv2.imshow('image',i)

cv2.waitKey()
cv2.destroyAllWindows()