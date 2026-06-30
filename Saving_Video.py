import cv2

video=cv2.VideoCapture('images/yolo_test.mp4')

width=int(video.get(3))
height=int(video.get(4))

output=cv2.VideoWriter('video_test.avi',cv2.VideoWriter_fourcc(*'XVID'),30,(width,height))

while True:
    status,frame=video.read()
    if not status:
        print('Video ended')
        break
    cv2.imshow('frame',frame)

    if cv2.waitKey(50) &0xFF==ord('q'):
        break
output.release()
cv2.destroyAllWindows()

