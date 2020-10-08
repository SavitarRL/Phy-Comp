# Research initial velocities of balls
# Research angular velocities of balls
# Outcome: possible values of diamter, d 
# using equation 12
import numpy as np
import sys
import matplotlib.pyplot as plt
import math
m_r = 200/1000  # 150g - 250g  #def as 200g
m_b = 2.7/1000  # mass of ball #def as 2.7g
v = 25          # in mph       #def as 25mph, converted below
omega = 36.8*2*(math.pi)
vel = (v / 1.609 * 1000) / (1*3600) #from mph to mps

d = ((3*m_r*vel)/(m_b*omega)) *1000

w = ((3*m_r*vel)/(m_b*(41.88/1000)*2*math.pi))

print(float(w))
print(float(d))