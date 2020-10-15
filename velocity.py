import math as m
import numpy as np
import matplotlib.pyplot as plt

mu = 1.9 * 10 ** (-5)               #dynamical viscosity of air
rho = 1.2754                        #density of air
C_D = 0.47                          #drag coefficient
m_b = 2.7/1000                      #mass of ball
t = 0.5                             #time elapsed in one "rally"
v_0 = 15                            #initial velocity
dialist = [0.038, 0.040, 0.042, 
           0.044, 0.046, 0.048, 0.05, 0.055 , 0.060,
           0.065, 0.070, 0.075, 0.080, 0.09, 0.1]     
                                    #list of diameters to be tested
ydotlist = []
for d in dialist:
    k = rho * C_D * m.pi *d**2      #determination of c1 as per eq 28
    yc1 = 8*m_b/(k) - 15
    ydot = 8*m_b/k - yc1*m.exp(3*k/(40*m_b)) * t
    idx = dialist.index(d)
    ydotlist.append(ydot)
    print(" {}. diameter: {} | velocity {:.3f}".format(
        idx + 1,
        d*1000,
        ydot))
plt.plot(dialist, ydotlist)
plt.title ("Velocity at t=0.5s in the y direction vs diameter")
plt.ylabel("V (m/s)")
plt.xlabel("diameter (m)")
plt.show()