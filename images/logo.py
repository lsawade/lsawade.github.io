#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import KDTree
from copy import deepcopy

def gaussian(t, to, sig, amp):
    """Create Gaussian pulse.

    :param t: time vector
    :param to: time in the center
    :param sig: standard deviation
    :param amp: amplitude
    :return: vector with same size of t containing the corresponding pulse

    """
    return amp * np.exp(-0.5 * (t-to)**2 / (sig * sig))


def bimodal_gaussian(t, amp1=2.5, to1=20, sig1=5, amp2=1.75, to2=32, sig2=3):
    """ Creates bimodal gaussian from gaussian function.

    :param t: time vector
    :param amp1: amplitude of first gaussian
    :param to1: center time of first gaussian
    :param sig1: standard deviation of first gaussian
    :param amp2: amplitude of second gaussian
    :param to2: center time of second gaussian
    :param sig2: standard deviation of second gaussian
    :return:
    """

    g1 = gaussian(t, to1, sig1, amp1)
    g2 = gaussian(t, to2, sig2, amp2)

    return g1 + g2

# Create wavelet
amp1=-1
to1=50
sig1=50
amp2=0.75
to2=-50
sig2=30
t = np.linspace(-500,500,1000)
wavelet = bimodal_gaussian(t, amp1, to1, sig1, amp2, to2, sig2)/2

plt.figure()
plt.plot(t,wavelet)

# Create Grid vectors
x = np.arange(-5, 1005,1, dtype=np.float)
y = np.arange(0, 1026, 20, dtype=np.float)
xx,yy = np.meshgrid(x,y)

yy_base = deepcopy(yy)

# Add spikes to locations
def compute_distance(x0,y0,x1,y1):
    """takes two location vectors computes there distance from each element
    in the first location to the elements in the second returning the element
    from location one that is closet to location 2.

    This is done using a kdtree algorithm."""

    # Create point arrays
    xy0 = np.array([[*x0],[*y0]]).T
    xy1 = np.array([[*x1],[*y1]]).T
    
    # Create kdtree
    mytree = KDTree(xy0)
    dist, indexes = mytree.query(xy1)

    return indexes[np.argmin(dist)]
    
# Create spikes first create circle
l = np.linspace(0, 1000, yy.shape[0])
xe0=np.round(2*(l-500)**3/np.max(l)**1.8 - 1.25*(l-500)  + 500).astype(int)
ye0=l

# Populate the lines in the right locations and concolve
for _i in range(xx.shape[0]):
    # ind = compute_distance(xx[_i,:], yy[_i,:], xe0, ye0)

    # 
    addyy = np.zeros(yy[_i, :].shape, dtype=np.float)
    factor = 3 - 3*(( _i - .5 * xx.shape[0] )/(.5*xx.shape[0]))**2
    addyy[xe0[_i]] = factor*3*1000/yy.shape[0]
    yy[_i, :] = yy[_i, :] +  np.convolve(addyy, wavelet, 'same')

    # 
    r = 503
    x0 = 500
    y0 = 500
    c = np.sqrt( r**2 - (y[_i]-y0)**2 )
    pos = np.where(np.logical_or(x0 - c > xx[_i, :], xx[_i, :] > x0 + c ))
    yy[_i, pos] = np.nan
    


plt.figure()
N = xx.shape[0]
for _i in range(N-1, -1, -1):
    plt.fill_between(xx[_i,:], yy[_i,:], y2=0, where=yy[_i,:]>0,  color='w', linewidth=2, zorder=N-_i)
    plt.plot(xx[_i,:], yy[_i,:], 'k', linewidth=1.5, zorder=N-(_i-0.5))
# plt.plot(xe0, ye0, 'k')
plt.axis('off')
plt.axis('equal')
plt.xlim([-5,1010])
plt.ylim([-5,1010])
plt.savefig("logo.pdf")
plt.show(block=True)



