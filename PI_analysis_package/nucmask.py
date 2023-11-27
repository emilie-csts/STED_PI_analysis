#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 17:02:58 2022

@author: christine
"""

import numpy as np
from scipy import ndimage
import skimage.filters as skfilt
from skimage import morphology


def nucleus_mask(img, gaussstd_nm=500, pxs_nm=15, num_di=0, num_er=0):

# gaussian smoothing of the image
    gaussstd = gaussstd_nm/pxs_nm
    img = ndimage.gaussian_filter(img, gaussstd)

    binary = img > skfilt.threshold_otsu(img)+0.02#-np.std(img)
    
    for i in range(0,num_er):
        binary = ndimage.binary_erosion(binary)

    
    
    for i in range(0,num_di):
        binary = ndimage.binary_dilation(binary)
    
    binary = ndimage.binary_fill_holes(binary)

    # remove stray background dots
    binary = morphology.remove_small_objects(binary, 20000)

    return binary


def nucleus_focus_mask(img, gaussstd_nm=500, pxs_nm=15, num_di=12, num_er=5):

# apply low pass filter to decrease out-of-focus contribution
    img = skfilt.difference_of_gaussians(img, low_sigma=0, high_sigma=gaussstd_nm/pxs_nm)
    img[img < 0] = 0  # remove any negative values in the image

# gaussian blurring of the image
    gaussstd = gaussstd_nm/pxs_nm
    img = ndimage.gaussian_filter(img, 1.2*gaussstd)

# thresholding and segmentation
    binary = img > skfilt.threshold_otsu(img)*1.2 #-np.std(img)
    
    for i in range(0,num_er):
        binary = ndimage.binary_erosion(binary)
    
    for i in range(0,num_di):
        binary = ndimage.binary_dilation(binary)
    
# remove stray background dots
    binary = morphology.remove_small_objects(binary, 20000)

    return binary
