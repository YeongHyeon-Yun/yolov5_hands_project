import cv2
import os
import time
import numpy as np


cap = cv2.VideoCapture(0)

keys = {
    ord('a'):'left',
    ord('s'):'right',
    ord('d'):'up',
    ord('f'):'down',
    ord('g'):'five',
    ord('j'):'zero',
}

while(True):
    ret, image = cap.read()
    if not ret:
        break
    cv2.imshow('src', image)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    if key in keys:
        l_txt = keys[key]
        d_txt = time.strftime('%y%m%d_%H%M%S')
        cv2.imwrite('saved/' + l_txt + '_' + d_txt + '.jpg', image)