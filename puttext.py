import cv2
image=cv2.imread('images/Chaithanya.jpeg')
text_on_image='Chaithanya'
font=cv2.FONT_HERSHEY_TRIPLEX
cv2.putText(image,text_on_image,(400,100),font,1,(255,0,0),2)
cv2.imshow('image',image)
cv2.waitKey()
cv2.destroyAllWindows()








