import numpy as np
import cv2
img=cv2.imread('images//cameraman.tif')
filtr=np.ones((3,3),np.int32)

erosion=cv2.erode(img,filtr)

dilation=cv2.dilate(img,filtr)

cv2.imshow('original',img)
cv2.imshow('erosion',erosion)
cv2.imshow('dilation',dilation)
cv2.waitKey()
cv2.destroyAllWindows()