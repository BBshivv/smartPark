import cv2
import pickle
import numpy as np
import cvzone
width,height=107,48
with open("carparkpos", "rb") as f:
    poslist = pickle.load(f)
cap = cv2.VideoCapture(r'carPark.mp4')
while(True):
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    success,img=cap.read()
    cv2.imshow("imagemain",img)
    cv2.waitKey(12)