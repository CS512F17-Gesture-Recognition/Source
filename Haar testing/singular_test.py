#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:42:10 2017

@author: ron
"""

import cv2
import sys
import os

def main():
    if len(sys.argv) !=4:
        raise ValueError("Missing arguments")
    path = sys.argv[1]
    cascade_path = sys.argv[2]
    neighbors = int(sys.argv[3])
    if not os.path.exists(path):
        raise ValueError("Invalid path or image file doesn't exist")
    if not os.path.exists(cascade_path):
        raise ValueError("Invalid path or cascade file doesn't exist")

    
    image = cv2.imread(path)
    cascade = cv2.CascadeClassifier(cascade_path)
    hand = cascade.detectMultiScale(image,minNeighbors = neighbors,minSize = (400,400))
    for x,y,w,h in hand:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('Image',image)
    k = cv2.waitKey(0)
    if k == ord('e'):
        cv2.destroyAllWindows()
    print("Did the detector mark the ROI properly? [Y/N]:")
    ans = input()
    if ans == 'y' or ans == 'Y':
        with open('accuracy.txt','a') as f:
            f.write('1\n')
    elif ans == 'n' or ans =='N':
        with open('accuracy.txt','a') as f:
            f.write('0\n')
    
    
if __name__ == "__main__":
    main()
    

        