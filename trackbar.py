import numpy as np
import cv2
def fun(event,x_cor,y_cor,alpha,beta):
    if event==cv2.EVENT_LBUTTONDOWN:
        text_on_img=str(x_cor)+","+str(y_cor)
        font = cv2.FONT_HERSHEY_PLAIN
        #cv2.putText(img,text_on_img,(x_cor,y_cor),font,2,(0,0,255),2)
        cv2.rectangle(img,(355,518),(484,615),(0,0,255),-1)
        #cv2.rectangle(img,(238,232),(362,288),(0,0,0),-1)
        #cv2.rectangle(img,(198,198),(358,397),(255,255,255),-1)
        cv2.imshow('image', img)
img=cv2.imread('images/messi.jpg')
cv2.imshow('image',img)
cv2.setMouseCallback('image',fun)

cv2.waitKey()
cv2.destroyAllWindows()