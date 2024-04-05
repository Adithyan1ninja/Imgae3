#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:50:35 2024

@author: ai-1
"""

import cv2 as cv
import numpy as np

img=cv.imread('walking.jpg')
x,y,c=img.shape
print(x,y)
my=y/10
my=int(my)
m=x/10
m=int(m)
print(m)
img[0:m,0:y]=[0,0,0]
img[x-m:x,1:y]=[0,0,0]

img[0:x,0:my]=[0,0,0]
img[0:x,y-my:y]=[0,0,0]
cv.imshow('img',img)
cv.waitKey(0)