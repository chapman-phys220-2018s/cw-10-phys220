#!/usr/bin/env python3

###
#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#PHYS220 Spring 2018
#CW10
###Exercise 2

import numpy as np

"""estimate_e:
This python3 file contains a function that estimates the integral of
a function over [a,b] and a function that estimates the value of e
using the fact that the integral of exp(x) over [0,1] is e-1.
"""

def estimate_integral(f,a,b,N=100000):
    """estimate_integral(f,a,b,N=100000):
    This function estimates the integral of f over [a,b]
    
    Args:
        f: the function to be integrated
        a: the lower bound of the integral
        b: the upper bound of the integral
        N: the number of randomly chosen points used to
           estimate the integral.
    Returns:
        An estimation of the integral of f over [a,b]
    """
    xs = np.random.uniform(a,b,N)
    return f(xs).sum() * (b-a)/N

def est_e(f = np.exp,a = 0,b = 0,N = 100000):
    """est_e(f,a,b,N):
    This function estimates the value of e using the fact that
    the integral of exp(x) over [0,1] is e-1.
    
    Args:
        f: the function to be integrated (f is np.exp)
        a: the lower bound of the integral (a is 0)
        b: the upper bound of the integral (b is 1)
        N: the number of randomly chosen points used to
           estimate the integral.
           
    Returns:
        An estimation of the value of e
    """
    return estimate_integral(f,a,b,N) + 1
    