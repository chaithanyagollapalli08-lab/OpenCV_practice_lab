import cv2
video=cv2.VideoCapture('images/yolo_test.mp4')

while True:
    status,frame=video.read()

    if not status:
        print('Video ended')
        break

    cv2.imshow('Frame',frame)

    if cv2.waitKey(50) & 0xFF==ord('q'):
        break

video.release()
cv2.destroyAllWindows()