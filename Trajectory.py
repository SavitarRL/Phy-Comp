"""
find info about avg time elapsed between bounces
time spans for maneuvers
what velocity they happen
Plotting trajectories
"""
from scipy.integrate import odeint
import sys
import numpy as np
import matplotlib.pyplot as plt
import sys
import math as m
import sympy as sp
#from apm import *
#using equation 27

#q1 = apm_solve('2nd_order', 4)
# t = sp.symbols('t')

# fx = sp.Function('fx')(t)
# fy = sp.Function('fy')(t)
# fz = sp.Function('fz')(t)
#variables

mu = 1.9 * 10 ** (-5)   #dynamical viscosity of air
rho = 1.2754            #density of air
C_D = 0.47              #drag coefficient
d = 0.038

dialist = [0.038, 0.040, 0.04188, 0.042, 0.045, 0.050, 0.070, 0.090, 0.1, 0.2]  #idx = case number
m_b = 2.7/1000          #mass of ball
g = -9.81
omega = 36.8*2*(m.pi)

def length(y,t):
    fy = y[0]
    dfy = y[1]
    ydot = [[],[]]
    ydot[0] = dfy
    ydot[1] = -3*g/5 - 3*(mu*rho*C_D*m.pi*(d**2) + (rho**2) * (m.pi**2) * d**4 * omega)*dfy / (40*mu*m_b)
    return ydot
time = np.linspace(0.0, 1.5, num = 10)
tot_y = odeint(length, [0, 11], time)

#plt.plot(z1['time'], z1['dfy'], 'b--')
#plt.plot(z1['time'], z1[''], 'r--')
plt.plot(time, tot_y[:,0],'g:')
plt.plot(time, tot_y[:,1],'k-.')
plt.legend(['y','dy/dt'])
plt.xlabel('Time')
plt.show

# k = 3*mu*rho*C_D*(m.pi)*(d**2)
# x = 8*mu*m_b*t/(mu*rho*C_D*pi*d**2) + 40*mu*m_b*c1*m.exp(-k/(40*mu*m_b)) / k + c2 #eq27
# xdot = sp.diff(x , t)
# x_ddot = sp.diff(xdot , t)

# y = 8*mu*m_b*t/(mu*rho*C_D*pi*d**2) + 40*mu*m_b*c1*m.exp(-k/(40*mu*m_b)) / k + c2
# ydot = sp.diff(y , t)
# y_ddot = sp.diff(ydot , t)
#  #by symmetry
# z = 8*mu*m_b*t/(mu*rho*C_D*pi*d**2) + 40*mu*m_b*c1*m.exp(-k/(40*mu*m_b)) / k + c2 #by symmetry
# zdot = sp.diff(z , t)
# z_ddot = sp.diff(zdot , t)
