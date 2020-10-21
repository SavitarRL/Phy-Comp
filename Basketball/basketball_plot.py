import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import math as m
import csv

def sim1():
    with open('Simulation Basketball 1.csv') as f:
        csv_reader = csv.reader(f, delimiter= ',')
        time = []
        x_pos1 = []
        y_pos1 = []
        z_pos1 = []
        vel1 = []
        position = []
        next(csv_reader, None)
        for row in csv_reader:
            t = float(row[0])
            time.append(t)
            v = float(row[4])
            vel.append(v)
            x = float(row[13])
            x_pos.append(x)
            y = float(row[14])
            y_pos.append(y)
            z = float(row[15])
            z_pos.append(z)
            r = np.sqrt(x**2 + y**2 + z**2)
            position.append(r)
        #print(time)
        #print(x_pos)
        #print(y_pos)
        #print(z_pos)
        #print(vel)
        plt.subplot(2,1,1)
        plt.plot(time, vel,'r')
        plt.title("Plot of velocity vs time")
        plt.ylabel("Velocity(m/s)")
        plt.xlabel("Time(s)")
        plt.grid(True)
        plt.xticks(np.arange(0,1.1,step = 0.1 ))
        
        plt.subplot(2,1,2)
        plt.plot(y_pos1, z_pos1, 'b-')
        plt.ylabel("Position in z direction (m)")
        plt.xlabel("Position in y direction (m)")
        plt.grid(True)
        plt.text(6.2,-0.206,'Scoring point')
        plt.xticks(np.arange(min(y_pos), max(y_pos)+0.5, step = 0.5))
        plt.show()
def sim2():
     with open('Simulation Basketball 2.csv') as f:
        csv_reader = csv.reader(f, delimiter= ',')
        time = []
        x_pos = []
        y_pos = []
        z_pos = []
        vel = []
        position = []
        next(csv_reader, None)
        for row in csv_reader:
            t = float(row[0])
            time.append(t)
            v = float(row[4])
            vel.append(v)
            x = float(row[13])
            x_pos.append(x)
            y = float(row[14])
            y_pos.append(y)
            z = float(row[15])
            z_pos.append(z)
            r = np.sqrt(x**2 + y**2 + z**2)
            position.append(r)
        #print(time)
        #print(x_pos)
        #print(y_pos)
        #print(z_pos)
        #print(vel)
        plt.subplot(2,1,1)
        plt.plot(time, vel,'r')
        plt.title("Plot of velocity vs time")
        plt.ylabel("Velocity(m/s)")
        plt.xlabel("Time(s)")
        plt.grid(True)
        plt.xticks(np.arange(0,1.1,step = 0.1 ))
        
        plt.subplot(2,1,2)
        mark = 6.2
        plt.plot(y_pos, z_pos, 'b-')
        plt.ylabel("Position in z direction (m)")
        plt.xlabel("Position in y direction (m)")
        plt.grid(True)
        plt.text(6.2,-0.206,'Scoring point')
        plt.xticks(np.arange(min(y_pos), max(y_pos)+0.5, step = 0.5))
        plt.show()

if __main__ = "__name__":
    sim1()
    sim2()