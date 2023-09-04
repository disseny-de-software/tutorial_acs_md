#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:42:14 2023

@author: joan
"""
from skimage.io import imread, imsave
import matplotlib.pyplot as plt
import numpy as np

for i in range(1,10):
    ima = imread('res{}.png'.format(i))
    ima = ima[:,:,:3]
    ima = ima[189:714, 1078:1437,:]
    ima[0,:,:] = 0
    ima[:,0,:] = 0
    ima[-1,:,:] = 0
    ima[:,-1,:] = 0
    #plt.imshow(ima), plt.axis('off')
    imsave('seq{}.png'.format(i), ima)

# ara fer convert -delay 100 seq*.png sequence.gif
