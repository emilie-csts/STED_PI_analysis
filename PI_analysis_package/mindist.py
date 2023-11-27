#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 13:35:54 2023

@author: christine
"""
import numpy as np
from scipy.spatial.distance import cdist


def shorter_dist(pt,others):
    distances = cdist(pt,others,'minkowski')
    min_distance = np.min(distances)
    return min_distance


def closest_point(pt,others):
    distances = cdist(pt,others,'minkowski')
    min_coord = others[distances.argmin()]
    return min_coord