#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 23:59:43 2017

@author: ron
"""

import cv2

def nothing():
    pass


def main():
    
    cap = cv2.VideoCapture(0)
    cascade_palm = cv2.CascadeClassifier("data/cascade_palm/cascade.xml")
    cascade_one = cv2.CascadeClassifier("data/cascade_1_finger/cascade.xml")
    cascade_two = cv2.CascadeClassifier("data/cascade_2_fingers/cascade.xml")
    cv2.namedWindow("Image",cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("Detection Parameters",cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("Neighbors (Palm)","Detection Parameters",40,50,nothing)
    cv2.createTrackbar("Neighbors (One Finger)","Detection Parameters",40,100,nothing)
    cv2.createTrackbar("Neighbors (Two Fingers)","Detection Parameters",65,100,nothing)
    cv2.createTrackbar("Window Size (x10)","Detection Parameters",40,100,nothing)

    while True:
        ret, frame = cap.read()
        if ret:
            n = cv2.getTrackbarPos("Window Size (x10)","Detection Parameters") *10
            neighbors1 = cv2.getTrackbarPos("Neighbors (Palm)","Detection Parameters")
            neighbors2 = cv2.getTrackbarPos("Neighbors (One Finger)","Detection Parameters")
            neighbors3 = cv2.getTrackbarPos("Neighbors (Two Fingers)","Detection Parameters")
            palm = cascade_palm.detectMultiScale(frame,minNeighbors = neighbors1,minSize = (n,n))
            one = cascade_one.detectMultiScale(frame,minNeighbors = neighbors2,minSize = (n,n))
            two = cascade_two.detectMultiScale(frame,minNeighbors = neighbors3,minSize = (n,n))
            print("Palm: %d, One: %d"%(len(palm),len(one)))
            for x,y,w,h in palm:
                print("(%d, %d, %d ,%d)"%(x,y,w,h))
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            for x,y,w,h in one:
                print("(%d, %d, %d ,%d)"%(x,y,w,h))
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
            for x,y,w,h in two:
                print("(%d, %d, %d ,%d)"%(x,y,w,h))
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            f1 = 'Minimum Neighbors: '+str(neighbors1)+', '+str(neighbors2)+', '+str(neighbors3)
            f2 = 'Detection Window: '+str(n)+'x'+str(n)
            
            if len(palm) > 0:
                cv2.putText(frame,"Detecting Palm",(1,100), font, 0.5,(0,255,0),2,cv2.LINE_AA)
            if len(one) > 0:
                cv2.putText(frame,"Detecting One Finger",(1,100), font, 0.5,(0,0,255),2,cv2.LINE_AA)
            if len(two) > 0:
                cv2.putText(frame,"Detecting two Fingers",(1,100), font, 0.5,(255,0,0),2,cv2.LINE_AA)
            
            cv2.putText(frame,f1,(1,50), font, 0.5,(0,255,255),2,cv2.LINE_AA)
            cv2.putText(frame,f2,(1,75), font, 0.5,(0,255,255),2,cv2.LINE_AA)
            cv2.imshow("Image",frame)
            k = cv2.waitKey(30)
            if k == ord('e'):
                cv2.destroyAllWindows()
                break
    
if __name__ == "__main__":
    main()