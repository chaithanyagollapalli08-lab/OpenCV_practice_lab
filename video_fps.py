import cv2
video=cv2.VideoCapture('images/yolo_test.mp4')
fps=video.get(cv2.CAP_PROP_FPS)
frame_count=int(video.get(cv2.CAP_PROP_FRAME_COUNT))
duration=frame_count/fps
print('frame per second :',fps)
print('total frames :',frame_count)
print('total seconds :',duration)
