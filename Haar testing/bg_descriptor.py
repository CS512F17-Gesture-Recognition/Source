#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 18:23:32 2017

@author: ron
"""
import os

def main():
        
    for img in os.listdir('neg'):
        if img.endswith('.jpg'):
            line = 'neg/'+img+'\n'
            with open('bg.txt','a') as f:
                f.write(line)
            
if __name__ == "__main__":
    main()