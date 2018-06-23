# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 18:41:32 2018

@author: chidan
"""
import numpy as np
import numpy.linalg as m
a = np.arange(18).reshape((2,3,3))
d= np.linalg.det(a)
print(d)