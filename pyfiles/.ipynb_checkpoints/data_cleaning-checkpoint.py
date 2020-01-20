"""DOCSTRING:

This module contains functions to upscale, downscale and prepare different xarray datasets in order to merge them into a final dataset.

"""
import pandas as pd
import xarray as xr
import numpy as np
import scipy.interpolate
import scipy.ndimage as ndimage

def scale_variable(variable, scaling_factors, mode = 'nearest', order = 0):
    """This function upscales a given input variable in an xarray Dataset, 
    and outputs the variable as an array with the same lat and lon dimensions as (6312, 1899) using scipy's ndimage.zoom function
    
    param_ds: the xarray dataset
    param_variable: a string of the variable name to upscale or downscale in the xarray dataset
    param_scaling_factors: a tuple of the values used to upscale or downscale the variable in order to output as lat lon dimensions of (6312, 1899). 
                            This is calculated based on the current dimensions of the variable. 
    param_mode: the mode parameter determines how the input array is extended beyond its boundaries
    param_order: order of the spline interpolation. Bilinear interpolation would be order=1, nearest is order=0, and cubic is the default (order=3)
    
    See https://docs.scipy.org/doc/scipy/reference/tutorial/interpolate.html for more details on documentation
    See http://scipy.github.io/devdocs/generated/scipy.ndimage.zoom.html#scipy.ndimage.zoom
    
    """
    var_ = ndimage.zoom(variable, (scaling_factors), mode = mode, order = order)
    return var_
