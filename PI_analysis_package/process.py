#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 16:53:11 2022

@author: christine
"""

import numpy as np
from scipy import ndimage

def process(img,gf_nm=10,pxs_nm=15):
    ## Standardize
    a = np.quantile(img,0.01)
    b = np.quantile(img,0.99)
    stretch = img
    stretch[img<a]=a
    stretch[img>b]=b

    ## Normalize images (to min/max)
    std = (stretch-np.min(stretch))/(np.max(stretch)-np.min(stretch))

    ## Denoise
    smoothed = ndimage.filters.gaussian_filter(std, sigma=gf_nm/pxs_nm)
    #smoothed = std
    return smoothed
