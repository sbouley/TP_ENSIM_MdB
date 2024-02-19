# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:33:50 2024

@author: Simon Bouley, simon.bouley@microdb.fr
"""


from matplotlib.pyplot import imread
import numpy as np
import matplotlib.pyplot as plt

def plot_CBF(b_grid, grid, path):
    
    """
    Parameters
    ----------
    b_grid : array (51 x 31)
        Value of the beamforming map on each calculation nodes (shape : 51 x 31)
    grid : array (51 x 31)
        Coordinates of the calculation grid (shape : 51 x 31)
    path : string
        path to DATA repository

    Returns
    -------
    None.

    """
    dyn = 8
    p_ref = 2e-5
    carto_dB = 20*np.log10((abs(b_grid))/p_ref)
    
    guitar_picture = 'photo_guitar.jpg'
    
    Z1 = imread(path + '//' + guitar_picture)
    extent = [min(grid[:,0]),max(grid[:,0]),min(grid[:,1]),max(grid[:,1])]
       
    plt.figure()
    plt.imshow(Z1, cmap=plt.cm.gray, interpolation='nearest', extent=extent) 
    plt.imshow(np.flipud(carto_dB.T), cmap='hot_r', alpha=0.5, interpolation='bilinear', vmin=np.amax(carto_dB)-dyn, vmax = np.amax(carto_dB), extent=extent)   
    plt.title(' CBF (dB, ref 2e-5 Pa)')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    plt.colorbar()
    
    
def plot_PSF(psf_grid, grid):
    
    """
    Parameters
    ----------
    psf_grid : array (51 x 31)
        Value of the point spread function in reference of one calculation nods (shape : 51 x 31)
    grid : array (51 x 31)
        Coordinates of the calculation grid (shape : 51 x 31)

    Returns
    -------
    None.

    """
    
    
    psf_dB = 20*np.log10((abs(psf_grid)))
    psf_dB_max = np.amax(psf_dB)
    extent = [min(grid[:,0]), max(grid[:,0]), min(grid[:,1]), max(grid[:,1])]
    
    plt.figure()
    plt.imshow(np.flipud(psf_dB.T) - psf_dB_max, interpolation='bilinear', extent=extent)   
       
    plt.title('PSF (dB)')
    plt.xlabel('x (cm)')
    plt.ylabel('y (cm)')
    plt.colorbar()