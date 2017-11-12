#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 12:24:25 2017

@author: ron
"""

import cv2
import numpy as np
    cW

def nothing():
    pass

def main():
    cv2.namedWindow("Capture Window",cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("ROI",cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("Thresholds",cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("Thresh","Thresholds",0,255,nothing)
    cv2.createTrackbar("Max Val","Thresholds",0,255,nothing)
    camera = cv2.VideoCapture(0)
    i = 0
    while True:
        flag, frame = camera.read()
        if flag:
            h,w = int(frame.shape[0]/2),int(frame.shape[1]/2)
            f = frame
            cv2.rectangle(f,(w-200,h-200),(w+200,h+200),(0,255,0),2)
            cv2.imshow("Capture Window",frame)
            cv2.imshow("ROI",f)
            k = cv2.waitKey(5)
            if k == ord('e'):
                cv2.destroyAllWindows()
                break
            if k == ord('c'):
                ROI = frame[(h-200):(h+200),(w-200):(w+200)]
                cv2.imwrite("../data/positiveImages/pos-"+str(i)+".jpg",ROI)
                print("Image Written")
                i+=1
                
if __name__ == "__main__":
    main()
                