import cv2
image=cv2.imread('images/Chaithanya.jpeg')
cv2.line(image,(250,500),(700,500),(0,255,0),2)
cv2.line(image,(470,180),(490,650),(0,0,255),2)
cv2.imshow('image',image)
cv2.waitKey()
cv2.destroyAllWindows()