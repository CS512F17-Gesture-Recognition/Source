#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 20:15:18 2017

@author: ron
"""

import cv2

def boundCountours(image):
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    ret,thresh1 = cv2.threshold(blur,60,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    ig, contours, hierarchy = cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    max_area=0
    ci=0
    for i in range(len(contours)):
        cnt=contours[i]
        area = cv2.contourArea(cnt)
        if(area>max_area):
            max_area=area
            ci=i
            cnt = contours[ci]
            hull = cv2.convexHull(cnt)

    cv2.drawContours(image,[cnt],0,(0,255,0),2)
    cv2.drawContours(image,[hull],0,(0,0,255),2)
    return image