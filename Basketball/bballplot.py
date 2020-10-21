import numpy as np
import matplotlib.pyplot as plt
import math as m
import csv

with open('Simulation Basketball 1.csv') as f:
    csv_reader = csv.reader(f, delimiter= ',')
    time = []
    x1_pos = []
    y1_pos = []
    z1_pos = []
    vel1 = []
    position1 = []
    next(csv_reader, None)
    for row in csv_reader:
        t = float(row[0])
        time.append(t)
        v1 = float(row[4])
        vel1.append(v1)
        x1 = float(row[13])
        x1_pos.append(x1)
        y1 = float(row[14])
        y1_pos.append(y1)
        z1 = float(row[15])
        z1_pos.append(z1)
        r1 = np.sqrt(x1**2 + y1**2 + z1**2)
        position1.append(r1)

with open('Simulation Basketball 2.csv') as g:
    csv_reader2 = csv.reader(g, delimiter= ',')
    x2_pos = []
    y2_pos = []
    z2_pos = []
    vel2 = []
    position2 = []
    next(csv_reader2, None)
    for row in csv_reader2:
        v2 = float(row[4])
        vel2.append(v2)
        x2 = float(row[13])
        x2_pos.append(x2)
        y2 = float(row[14])
        y2_pos.append(y2)
        z2 = float(row[15])
        z2_pos.append(z2)
        r2 = np.sqrt(x2**2 + y2**2 + z2**2)
        position2.append(r2)

#necessary angles
theta1 = m.atan(4.138405/7.087581)*180/m.pi
theta2 = m.atan(4.090675/6.34982)*180/m.pi
print(theta1, theta2)

#plotting velocity vs time
plt.plot(time, vel1, 'r', label = 'initial velocity = 8.21 m/s')
plt.plot(time, vel2, 'g', label = 'initial velocity = 7.55 m/s')
plt.title("Plot of velocity vs time")
plt.ylabel("Velocity(m/s)")
plt.xlabel("Time(s)")
plt.grid(True)
plt.xticks(np.arange(0,1.1,step = 0.1 ))
plt.yticks(np.arange(5.5,11,step = 0.5))
plt.legend(loc = "upper right")
plt.show()

#plotting y vs z
plt.plot(y1_pos, z1_pos, 'b', label = 'initial velocity = 8.21 m/s')
plt.plot(y2_pos, z2_pos,'y', label = 'initial velocity = 7.55 m/s')
plt.plot(6.2, -0.206,'k')
plt.ylabel("Position in z direction (m)")
plt.xlabel("Position in y direction (m)")
plt.grid(True)
plt.title("Plot of height(z) vs length to the ring(y)")
plt.text(6.2,-0.206,'Scoring point')
plt.xticks(np.arange(min(y1_pos), max(y1_pos)+0.5, 0.5))
plt.yticks(np.arange(-0.4, 0.9, step = 0.1 ))
plt.legend(loc = "lower left")
plt.show()
