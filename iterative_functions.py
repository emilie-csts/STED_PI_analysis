#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 09:57:37 2022

@author: christine
"""

import numpy as np
from scipy.optimize import curve_fit

### Lorentzian distribution
# This distribution is the best function to describe PSF obtained in STED.
# the number of parameters passed in argument should be a mutliple of 3 (a,xo,gamma) + 1 constant
# the number of parameters will allow to sum iteratively lorentzian functions
# if len(params)-1 = 3n the resulting function is the sum of n Lorentzians

def lorentzian(x,*params):
    if len(params)%3==1:
        c = params[-1]
        y = np.zeros(len(x))
        for i in range(0,len(params)-1,3):
            a = params[i]
            xo = params[i+1]
            gamma = params[i+2]
            y = y + a/(((x-xo)/(0.5*gamma))**2+1) 
        y = y+c
        return y
    else:
        return 'there are not enough parameters'
    




#######################################################################
### Gaussian distribution
# the number of parameters passed in argument should be a mutliple of 3 (a,xo,sigma) + 1 constant
# the number of parameters will allow to sum iteratively gaussian functions
# if len(params)-1 = 3n the resulting function is the sum of n Gaussians

def gaussian(x,*params):
    if len(params)%3==1:
        c = params[-1]
        y = np.zeros(len(x))
        for i in range(0,len(params)-1,3):
            a = params[i]
            xo = params[i+1]
            sigma = params[i+2]
            y = y + a*(1/(sigma*(np.sqrt(2*np.pi))))*(np.exp((-1.0/2.0)*(((x-xo)/sigma)**2)))
        y = y+c
        return y
    else:
        return 'there are not enough parameters'





#######################################################################
### Iterative fitting
# This function fits a set of data with a distribution of functions
# f=function (Lorentzian or Gaussian)
# nb_iterations = max number of summed functions (by default = 5)
# tolerance = level of significance for the null hypothesis (by default = 0.05)
# iterations stop when the R2 passes above 1-tol

   
def iterative_fit(f,xdata,ydata,nb_iterations=5,tol=0.05):
    n=0
    minB = []
    maxB = []
    labels_y = ['data']
    labels_r = ['zero']
    r_sq = 0
    goodness = 1-tol

    while n<nb_iterations and r_sq<goodness:

        n=n+1
        labels_y.append(n)
        labels_r.append(n)
        
        guess = np.zeros(3*n+1)
        minB = np.zeros(3*n+1)
        maxB = np.zeros(3*n+1)

        for i in range(0,3*n,3):
            guess[i]=np.max(ydata)
            guess[i+1]=((i+1)/(n+1))*(np.max(xdata)-np.min(xdata))
            guess[i+2]=(1/n)*(np.max(xdata)-np.min(xdata))

            maxB[i]=np.inf #np.max(ydata)*100
            maxB[i+1]=np.inf #np.max(xdata)
            maxB[i+2]= np.inf #10*(np.max(xdata)-np.min(xdata))

        maxB[-1]=np.inf
        lim=[minB,maxB]
        
        popt,pcov = curve_fit(f,xdata,ydata,p0=guess,bounds=lim)
        residuals = ydata - f(xdata,*popt)
        ss_res = np.sum((residuals)**2)
        ss_tot = np.sum((ydata-np.mean(ydata))**2)
        r_sq = 1-(ss_res/ss_tot)

        perr = np.sqrt(np.diag(pcov))
        
        
            
    return n, popt, pcov, r_sq, residuals
        
    