import cv2
image=cv2.imread('images/Chaithanya.jpeg')
cv2.circle(image,(475,360),15,(0,0,255),2)
cv2.imshow('image',image)
cv2.waitKey()
cv2.destroyAllWindows()