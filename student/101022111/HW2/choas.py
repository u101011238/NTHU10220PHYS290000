# -*- coding: utf-8 -*-
"""
Created on Mon Apr 21 23:33:08 2014

@author: larry lu
"""

from pylab import *
def choas():
    x=0.5
    r=arange(1,4,0.01)
    for i in range(1000):
        x=r*x*(1-x)
    plot(r,x)
    xlabel('r')
    ylabel('x')
    title('logistic map')
    show()

choas()
