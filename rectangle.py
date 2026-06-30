import cv2
image=cv2.imread('images/lena_color_512.tif')
cv2.rectangle(image,(15,300),(300,500),(255,255,255),-1)
cv2.imshow('image',image)
cv2.waitKey()
cv2.destroyAllWindows()
