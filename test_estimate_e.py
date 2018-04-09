#!/usr/bin/env python3

###
#Daniel Chang
#2260161
#Chang254@mail.chapman.edu
#PHYS220 Spring 2018
#CW10
###Exercise 2

import numpy as np
import estimate_e as ee
import nose

def test_estimate_e():
    trial = ee.est_e(np.exp,0,1,10000000000)
    actual = np.exp(1)
    print("Trial:", trial)
    print("Desired:", actual)
    nose.tools.assert_almost_equal(actual,trial,3)