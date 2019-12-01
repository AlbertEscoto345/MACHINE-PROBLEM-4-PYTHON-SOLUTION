from math import *
import matplotlib.pyplot as plt

y_initial=float(input("Input projectile's initial height above ground in meters: "))
if(y_initial==0):
    print ('Invalid input. Please try again.')
    
velocity=float(input("Input projectile's velocity in meters per second (m/s): "))
firing_angle=float(input("Input projectile's angle at which it was fired with respect to the x-axis in degrees: "))
radian_angle=radians(firing_angle)
x_accel=float(input("Input projectile's acceleration in the x-component in meters per second squared (m/s^2): "))
y_accel=float(input("Input projectile's acceleration in the y-component in m/s^2: "))

xAll=[]
yAll=[]
t=0
abscissa=0
ordinate=y_initial
disp=0.00001

x_velocity=velocity*cos(radian_angle)
y_velocity=velocity*sin(radian_angle)

xAll.append(abscissa)
yAll.append(ordinate)

while(y_velocity>0):
    t+=disp
    abscissa=x_velocity*t+(x_accel/2)*(t**2)
    ordinate=y_velocity*t+(y_accel/2)*(t**2)+y_initial
    xAll.append(abscissa)
    yAll.append(ordinate)
    if ordinate<=0:
        break

plt.plot(xAll, yAll)
