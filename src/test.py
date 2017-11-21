#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 23:59:43 2017

@author: ron
"""

import cv2
from visualize import boundCountours
import sys
import os

def nothing(x):
    pass


def main():
    '''
    Tests Gesture Detector through camera inputs or from a video file.
    [COMMAND LINE ARGUMENTS]:
        @param : Filename specifying video file for testing. If not used then
                camera is used as capture device
    '''
    assert len(sys.argv) <= 2, "Too Many Arguments"
    if len(sys.argv) == 2:
        device = sys.argv[1]
        if not os.path.exists(device):
            raise ValueError("File doesn't exist")
    else:
        device = 0
    
    f = open('help.txt')
    h = f.read()
    f.close()
    
    cap = cv2.VideoCapture(device)
    cascade_palm = cv2.CascadeClassifier("data/cascade_palm/cascade.xml")
    cascade_one = cv2.CascadeClassifier("data/cascade_1_finger/cascade.xml")
    cascade_two = cv2.CascadeClassifier("data/cascade_2_fingers_aug/cascade.xml")
    cv2.namedWindow("Image",cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("Detection Parameters",cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("Neighbors (Palm)","Detection Parameters",40,255,nothing)
    cv2.createTrackbar("Neighbors (One Finger)","Detection Parameters",40,255,nothing)
    cv2.createTrackbar("Neighbors (Two Fingers)","Detection Parameters",65,255,nothing)
    cv2.createTrackbar("Window Size (x10)","Detection Parameters",40,100,nothing)
    cv2.createTrackbar("Palm","Detection Parameters",0,1,nothing)
    cv2.createTrackbar("One Finger","Detection Parameters",0,1,nothing)
    cv2.createTrackbar("Two Fingers","Detection Parameters",0,1,nothing)
    font = cv2.FONT_HERSHEY_SIMPLEX


    while True:
        ret, frame = cap.read()
        if frame is None:
            exit()
        if ret:
            n = cv2.getTrackbarPos("Window Size (x10)","Detection Parameters") *10
            neighbors1 = cv2.getTrackbarPos("Neighbors (Palm)","Detection Parameters")
            neighbors2 = cv2.getTrackbarPos("Neighbors (One Finger)","Detection Parameters")
            neighbors3 = cv2.getTrackbarPos("Neighbors (Two Fingers)","Detection Parameters")
            DETECT_PALM = cv2.getTrackbarPos("Palm","Detection Parameters")
            DETECT_ONE = cv2.getTrackbarPos("One Finger","Detection Parameters")
            DETECT_TWO = cv2.getTrackbarPos("Two Fingers","Detection Parameters")
            
            if DETECT_PALM == 1:
                palm = cascade_palm.detectMultiScale(frame,minNeighbors = neighbors1,minSize = (n,n))
                if len(palm)>0:
                    for x,y,w,h in palm:
                        frame[x:x+w,y:y+h] = boundCountours(frame[x:x+w,y:y+h])
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                    cv2.putText(frame,"Detecting Palm",(1,100), font, 0.5,(0,255,0),2,cv2.LINE_AA)
           
            if DETECT_ONE == 1:
                one = cascade_one.detectMultiScale(frame,minNeighbors = neighbors2,minSize = (n,n))
                if len(one)>0:
                    for x,y,w,h in one:
                        frame[x:x+w,y:y+h] = boundCountours(frame[x:x+w,y:y+h])
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(frame,"Detecting One Finger",(1,100), font, 0.5,(0,0,255),2,cv2.LINE_AA)
            
            if DETECT_TWO == 1:
                two = cascade_two.detectMultiScale(frame,minNeighbors = neighbors3,minSize = (n,n))
                if len(two)>0:
                    for x,y,w,h in two:
                        frame[x:x+w,y:y+h] = boundCountours(frame[x:x+w,y:y+h])
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                    cv2.putText(frame,"Detecting two Fingers",(1,100), font, 0.5,(255,0,0),2,cv2.LINE_AA)
            
            f1 = 'Minimum Neighbors: '+str(neighbors1)+', '+str(neighbors2)+', '+str(neighbors3)
            f2 = 'Detection Window: '+str(n)+'x'+str(n)
            cv2.putText(frame,f1,(1,50), font, 0.5,(0,255,255),2,cv2.LINE_AA)
            cv2.putText(frame,f2,(1,75), font, 0.5,(0,255,255),2,cv2.LINE_AA)
            cv2.imshow("Image",frame)
            k = cv2.waitKey(30)
            if k == ord('e'):
                cv2.destroyAllWindows()
                break
            if k == ord('h'):
                print(h)
                
    
if __name__ == "__main__":
    main()
