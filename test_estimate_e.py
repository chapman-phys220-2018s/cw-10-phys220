#!/usr/bin/env python3

###
#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#Devon Ball
#2313078
#dball@chapman.edu
#Myranda Hoggatt
#2285495
#hogga102@mail.chapman.edu
#PHYS220 Spring 2018
#CW10
#Exercise 2
###

import numpy as np
import estimate_e as ee
import nose

"""test_estimate_e:
This python3 file contains a test function that tests the estimation
of e from the est_e function in the estimate_e python file.
"""

def test_estimate_e():
    """
    test_estimate_e():
    This tests the estimation of e by the est_e function against np.exp(1), which is
    equivalent to e, to 3 sig figs (or 2 decimal places).
    """
    trial = ee.est_e(np.exp,0,1,10000000)
    actual = np.exp(1)
    print("Trial:", trial)
    print("Desired:", actual)
    nose.tools.assert_almost_equal(actual,trial,2)