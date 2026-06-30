import cv2


img=cv2.imread('images/lena_color_256.tif',1)
h,w=img.shape[:2]
center=(w//2,h//2)
r=cv2.getRotationMatrix2D(center,45,1)
rotated=cv2.warpAffine(img,r,(w,h))
cv2.imshow('image',img)
cv2.imshow('rotate',rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()