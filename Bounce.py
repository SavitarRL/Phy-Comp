#bouncing analysis --> optimal diameter
"""
All 24 balls must rebound to a height of not less than 240mm and not more than 260mm when
dropped from a height of 305mm on to a standard steel block.
"""
import numpy as np
import matplotlib.pyplot as plt
import sys
import math as m

s = 1.3/1000    #thickness
h_1 = 0.305 #initial height
h_2 = 0.8*h_1   #final height
g = 9.81        #gravitatonal acceleration
m_b = 2.7/1000  #mass of ball
d_t = 0.025     #collsion time with the block
#using equation 8
d = (160*m.sqrt(10)+400*m.sqrt(2))*(s**2)/(d_t*m.sqrt(g*h_1))*1000
print(d)
