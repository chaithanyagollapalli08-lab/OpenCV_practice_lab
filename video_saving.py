import cv2
img_from_video=cv2.VideoCapture('images/yolo_test.mp4')

w=img_from_video.get(3)
h=img_from_video.get(4)
driver_name=cv2.VideoWriter_fourcc(*'XVID')
output=cv2.VideoWriter('images/yolo_test.mp4',driver_name,20,(int(w),int(h)))
c=0
while True:
    status,pixel=img_from_video.read()

    if status:
        c=c+1
        text='Frame'+str(c)
        font=cv2.FONT_HERSHEY_PLAIN
        cv2.putText(pixel,text,(50,50),font,10,(0,255,0),2)
        cv2.imshow('image',pixel)
        output.write(pixel)
        if cv2.waitKey(10) & 0XFF == ord('q'):
            break

    else:
        break



img_from_video.release()
output.release()
cv2.destroyAllWindows()