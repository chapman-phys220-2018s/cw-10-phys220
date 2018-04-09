#!/usr/bin/env python3

###
#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#PHYS220 Spring 2018
#CW10
###Exercise 2

import numpy as np

def estimate_integral(f,a,b,N=1000):
    xs = np.random.uniform(a,b,N)
    return f(xs).sum() * (b-a)/N

def est_e(f,a,b,N):
    return estimate_integral(f,a,b,N) + 1
    