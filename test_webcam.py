import cv2
import hands_detector
import numpy as np

cap = cv2.VideoCapture(0)
cat_list = ['left', 'right', 'up', 'down', 'five', 'zero']


while True:
    ret, src = cap.read()
    if not ret:
        break
    det = hands_detector.detect(src)
    if det is not None:
        dst = hands_detector.draw_boxes(src, det)
        
        print(det)
        
    else:
        dst = src.copy()
    cv2.imshow('dst', dst)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite('hands_photo.jpg', dst)