import cv2
img_from_video=cv2.VideoCapture('images/yolo_test.mp4')

while True:
    status,pixel=img_from_video.read()
    if not status:
        break
    cv2.imshow('image',pixel)
    if cv2.waitKey(30)& 0XFF==ord('q'):
            break

img_from_video.release()
cv2.destroyAllWindows()

