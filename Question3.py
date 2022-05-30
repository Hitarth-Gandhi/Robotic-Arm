import numpy as np 
import math 
import matplotlib.pyplot as plt
L1=1.2
L2=1.6
N_theta=5
Thetastart=0
Thetaend=34
Thetastart1=0
Thetaend1=22
theta1=[]
theta2=[]
y=[]
z=[]
for i in range(Thetastart,Thetaend,5):
 temp=math.radians(i)
 theta1.append(temp)
 y.append(i)

for i in range(Thetastart1,Thetaend1,5):
 temp=math.radians(i)
 theta2.append(temp)
 z.append(i)

x0=0
y0=0
figno=1
for t1 in theta1:
    for t2 in theta2:
        x1=L1*math.cos(t1)
        y1=L1*math.sin(t1)
        x2=x1+L2*math.cos(t2)
        y2=y1+L2*math.sin(t2)


        filename= str(figno)+ '.jpg'
        figno=figno+1

        plt.figure()
        plt.plot([x0,x1],[y0,y1])
        plt.plot([x1,x2],[y1,y2])
        plt.xlim([0,2])
        plt.ylim([0,2])
        plt.savefig(filename)



