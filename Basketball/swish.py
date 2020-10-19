import math as m
import numpy as np
import matplotlib.pyplot as plt

# need to find suitbale values of omega and v 
# plot the trajectory using found values
# w = omega for angular vel ; v = velocity

F_M = 5.537*10**(-3) * ((w*v**2)/(0.246*w+v)) #equation 3

F_D1 = (1.992*10**(-3)* w * v^2)/((2.842*10**(-2)*w**(5/2)+v**(5/2)))**(0.4)  #equation 12 
F_D = F_D1 + 1.581*10**(-2)*v**2 

