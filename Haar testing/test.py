#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 23:59:43 2017

@author: ron
"""

import cv2

cap = cv2.VideoCapture(0)
hand_cascade = cv2.CascadeClassifier("data/cascade.xml")

while True:
    ret, frame = cap.read()
    hand = hand_cascade.detectMultiScale(frame,minNeighbors = 10,minSize = (400,400))
    for x,y,w,h in hand:
        print("(%d, %d, %d ,%d)"%(x,y,w,h))
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Image",frame)
    k = cv2.waitKey(30)
    if k == ord('e'):
        cv2.destroyAllWindows()
        break
    
