#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 09:55:31 2023

@author: christine
"""

import numpy as np
from astropy.stats import sigma_clipped_stats
import photutils
from photutils.datasets import load_star_image
from photutils.detection import DAOStarFinder


def detect_pores(img, threshold, fwhm):
    
    daofind = DAOStarFinder(threshold, fwhm) 
    sources = daofind(img)  

    peaks_x = sources['xcentroid']
    peaks_y = sources['ycentroid']
    
    peaks = np.array([peaks_x,peaks_y])
        
    return peaks