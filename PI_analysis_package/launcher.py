#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Friday Novembre 10 2023

@author: emilie
"""
import os
import glob
import numpy as np
from datetime import datetime

# Define parameters
names = []
allimgs = False 

def data_launcher (dirpath, outputfolder):
    
    ## Set the date 
    now = datetime.now()
    #print("now =", now)

    ## Define the outputpath date folder --> it will create a folder by adding the date 
    date = now.strftime("%Y%m%d_%H-%M") # On Mac system: %H:%M
    #print("date and time =", date)	
    outputpathdate = outputfolder+'/'+date
    #print(outputpathdate)
    os.mkdir(outputpathdate)
    
    ## Load images paths
    if allimgs:
        files = glob.glob(os.path.join(dirpath, '*[0-9].tif'))
    
    else:
        files = [os.path.join(dirpath, '230127_Nup96_1')]
        # this path has to be changed depending on the file --> to be modified
    #print(files)

    for filepath in files:
        imgname = filepath.split('\\')[-1].split('.')[0] # I had to modify the way we split the name of the doc --> it is diff on windows
        names.append(imgname)

    unique_files=np.unique(names) 
    #print(unique_files)

    for imgname in unique_files:
        #print('image name = ',imgname)
        NupX_name = imgname.split('_')[1]
        #print('NupX = ',NupX_name)
        outputpath = outputpathdate+'/'+imgname
        #print('Outputtpath = ',outputpath)
        os.mkdir(outputpath)

    # Iterate through unique image file names
    for imgname in unique_files:
        #print('Image name:', imgname)
    # Extract NupX name from image name
        NupX_name = imgname.split('_')[1]
        #print('NupX:', NupX_name)
    # Create output directory for the current image
        outputpath = os.path.join(outputpathdate, imgname)
        #print('Output path:', outputpath)
    
    # File paths for mAB, POM, and NupX images
    mABpath = os.path.join(dirpath, imgname + '.msr_414' + '.tif')  
    POMpath = os.path.join(dirpath, imgname + '.msr_POM'  + '.tif')
    NupXpath = os.path.join(dirpath, imgname + '.msr_Nup96'  + '.tif')
    
    return(mABpath, POMpath, NupXpath,NupX_name,imgname)
