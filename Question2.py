import numpy as np 
import math
a1=float(input("enter a1"))
a2=float(input("enter a2"))
alpha1=(math.pi*float(input("enter alpha1")))/180
alpha2=(math.pi*float(input("enter alpha2")))/180
d1=float(input("enter d1"))
d2=float(input("enter d2"))
theta1=(math.pi*float(input("enter theta1")))/180
theta2=(math.pi*float(input("enter theta2")))/180
A1=np.array([[math.cos(theta1),-math.sin(theta1)*math.cos(alpha1),math.sin(theta1)*math.sin(alpha1),a1*math.cos(theta1)],[math.sin(theta1),math.cos(theta1)*math.cos(alpha1),-math.cos(theta1)*math.sin(alpha1),a1*math.sin(theta1)],[0,math.sin(alpha1),math.cos(alpha1),d1],[0,0,0,1]])
A2=np.array([[math.cos(theta2),-math.sin(theta2)*math.cos(alpha2),math.sin(theta2)*math.sin(alpha2),a1*math.cos(theta2)],[math.sin(theta2),math.cos(theta2)*math.cos(alpha2),-math.cos(theta2)*math.sin(alpha2),a1*math.sin(theta2)],[0,math.sin(alpha2),math.cos(alpha2),d2],[0,0,0,1]])
A3=A1.dot(A2)
print("the x coordinate is", A3[0,3])
print("the y coordinate is", A3[1,3])
print(A3) 