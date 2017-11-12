#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 19:35:02 2017

@author: ron
"""

import os
import sys

def main():
    assert len(sys.argv) == 5, "Missing Arguments"
    try:
        num = int(sys.argv[1])
        w = int(sys.argv[2])
        h = int(sys.argv[3])
        n = int(sys.argv[4])
    except:
        assert False, "Expected integer"
        
    if os.path.exists('sample_creator.sh'):
        os.remove('sample_creator.sh')
        
    with open('sample_creator.sh','a') as f:
        f.write("#! /bin/sh\n\n")
    for i in range(n):
        if i == n:
            break
        end = '' if i==n-1 else ' &&'
        line ='opencv_createsamples -img pos_burned/pos-'+str(i)+'_burned.jpg -bg bg.txt -info info/pos-'+ \
            str(i)+'_burned.txt -num '+ str(num)+ \
            ' -maxxangle 0.5 -maxyangle 0.5 -maxzangle 0.3 -bgcolor 255 -bgthresh 8 -w ' + \
            str(w)+' -h '+str(h)+end+'\n'
        with open('sample_creator.sh','a') as f:
            f.write(line)
            
if __name__ == "__main__":
    main()