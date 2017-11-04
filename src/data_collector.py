#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:15:32 2017

@author: ron
"""
import cv2
import numpy as np
import os
import re

def _nothing():
    """
    Does nothing. Only for trackbar callback.
    """
    pass

def _get_labels(flag=False):
    """
    Returns the currently selected label number.
    [PARAMETERS]:
        flag (bool) - If True then return only data set selector
    """
    if flag == False:
        label = cv2.getTrackbarPos("Label","interface")
    else:
        label = cv2.getTrackbarPos("Data Set","interface")
    return label

def _flattern_image(image):
    """
    Flatterns image into a vector.
    [PARAMETERS]:
        image (numpy.ndarray) - An RGB image.
    [RETURNS]:
        Flattened Image
    """
    flat = image.reshape(-1)
    return flat

def _save(data,labels):
    """
    Saves the currently accumulated dataset and labels.
    [PARAMETERS]:
        data (numpy.ndarray) - A 2-D array of images
        labels (numpy.ndarray) - A 1-D array of labels
    [RETURNS]:
        Nothing. Prints information about saved data.
    """
    flag = bool(_get_labels(True))
    labels = np.array(labels)
    data = np.array(data)
    
    if flag:
        #test
        files = os.listdir("../data/test/")
        if len(files)==0:
            data.dump("../data/test/data_1.dat")
            labels.dump("../data/test/label_1.dat")
        else:
            digit = int(re.findall("\d+",sorted(files,reverse=True)[0])[0])+1
            path_data = "../data/test/data_"+str(digit)+".dat"
            path_label = "../data/test/labels_"+str(digit)+".dat"
            data.dump(path_data)
            labels.dump(path_label)
            print("Data written to test folder with %d instances" %data.shape[0])
    else:
        #train
        files = os.listdir("../data/train/")
        if len(files)==0:
            data.dump("../data/train/data_1.dat")
            labels.dump("../data/train/label_1.dat")
        else:
            digit = int(re.findall("\d+",sorted(files,reverse=True)[0])[0])+1
            path_data = "../data/train/data_"+str(digit)+".dat"
            path_label = "../data/train/labels_"+str(digit)+".dat"
            data.dump(path_data)
            labels.dump(path_label)
            print("Data written to train folder with %d instances" %data.shape[0])
        
        
    

def data_collector(camera,width,height):
    """
    Collects training and testing data for gesture recognition and saves them in
    data/train and data/test respectively. The images are stored as a 2D matrix with
    each row 'i' a vector of length
    [PARAMETERS]:
        camera (cv2.VideoCapture) - A video capture object.
        width (int) - Width of saved image.
        height (int) - Height of saved image.
    [RETURNS]:
        Nothing
    """
    assert isinstance(width,int), "width not an integer"
    assert isinstance(height,int), "height not an integer"
    
    labels = []
    data = []
    
    while True:
        frame, image = camera.read()
        if frame:
            cv2.imshow("Capture",image)
            k = cv2.waitKey(15)
            if k == ord('c'):
                label = _get_labels()
                image = cv2.resize(image,dst = (width,height))
                flat = _flattern_image(image)
                data.append(flat)
                labels.append(label)
            elif k == ord('s'):
                _save(data,labels)
                labels = []
                data = []
            elif k == ord('e'):
                cv2.destroyAllWindows()

            
def main():
    """
    [USAGE]:
        1. Use the Interface Labels to select from the following class labels:
            Negative instance - Labeled as 0
            Closed Palm - Labeled as 1
            Open Hand - Labeled as 2
            One Finger - Labeled as 3
            Two Fingers - Labeled as 4
            Three Fingers - Labeled as 5
        2. Use the interface Dataset selector to select from test or train:
            0 - Training Data
            1 - Testing Data
        3. The following key presses are supported:
            c - Capture image and label for addition to datset
            s - Save the current dataset and labels
            e - Exit
    """
    cv2.namedWindow("Capture")
    cv2.namedWindow("TrackBar")
    cv2.createTrackbar("Interface","Label",0,5,_nothing)
    cv2.createTrackbar("Interface","Data Set",0,1,_nothing)
    camera = cv2.VideoCapture(0)
    data_collector(camera,640,480)
    
    
    
if __name__ == "__main__":
    main()