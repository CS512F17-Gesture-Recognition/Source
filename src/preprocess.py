#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:56:10 2017

@author: ron
"""
import numpy as np
import cv2

def skin_mask(image,kernel_size=3,erode_iter=1,dilate_iter=1,debug=False):
    """
    Performs foreground extraction, typically a hand using simple thresholds in
    YCrCb color space followed by morphological Opening (dilation of erosion).
    [PARAMETERS]:
        image (numpy.ndarray)- an RGB image 
        kernel_size (int)- Size of kernel used in filtering and morphology. Should be odd.
        erode_iter (int)- Number of erosion iterations to be performed.
        dilate_iter (int)- Number of dilation iterations to be performed.
        debug (bool)- If set to true then result of each operation is saved in the data folder
                    with filename starting with 'skin_mask'
    [RETURNS]:
        A binary mask of type np.ndarray
    """
    assert isinstance(image,np.ndarray), "Input not a numpy array"
    assert image.ndim == 3, "Expected 3 channels, got %d" %image.ndim
    assert isinstance(kernel_size,int) and isinstance(erode_iter,int) and isinstance(dilate_iter,int),"Optional argument not an integer"
    assert kernel_size%2!=0, "Kernel size not odd"
    kernel = np.ones((kernel_size,kernel_size),dtype=np.uint8)
    
    image_ycbcr = cv2.cvtColor(image,cv2.COLOR_BGR2YCR_CB)
    lower = np.array([90,105,130],dtype=np.uint8)
    upper = np.array([230,135,170],dtype=np.uint8)
    mask = cv2.inRange(image_ycbcr,lower,upper)
    mask = cv2.medianBlur(mask,kernel_size)
    output = cv2.erode(mask,kernel,iterations=erode_iter)
    output = cv2.dilate(output,kernel,iterations=dilate_iter)
    
    
    if debug:
        cv2.imwrite("data/skin_mask_input.jpg",image)
        cv2.imwrite("data/skin_mask_input_cvt.jpg",image_ycbcr)    
        cv2.imwrite("data/skin_mask_mask.jpg",mask)
        cv2.imwrite("data/skin_mask_output.jpg",output)
    return output
    

def find_countours(mask):
    """
    INCOMPLETE
    """
    
    mask,contours,hierarchy = cv2.findContours(mask)
    areas = [cv2.moments(x)['m00'] for x in contours]
    areas = np.argsort(areas)
    pass
