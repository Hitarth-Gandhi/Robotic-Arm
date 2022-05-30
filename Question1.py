import numpy as np 
import math
L1=int(input("Enter the length of Link 1"))
L2=int(input("Enter the length of link 2"))
Theta1=(math.pi*int(input("Enter the angle made by link 1 with ground")))/180
Theta2=(math.pi*int(input("Enter the angle between link 1 and link 2")))/180
X=((L1*math.cos(Theta1))+(L2*math.cos(Theta1+Theta2)))
Y=((L1*math.sin(Theta1))+(L2*math.sin(Theta1+Theta2)))
print("x coordinate =", X)
print("y coordinate =", Y)
