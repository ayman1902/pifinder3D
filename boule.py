# Import libraries
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import random as rd

def algoboule(n):
    # Creating dataset
    x1 = []
    x2 = []
    x3 = []
    y1 = []
    y2 = []
    y3 = []
    ni=0
    for i in range(n):
        p1 = rd.uniform(-1,1)
        p2 = rd.uniform(-1,1)
        p3 = rd.uniform(-1,1)
        if np.sqrt(p1**2+p2**2+p3**2)<1:
            ni+=1
            x1.append(p1)
            x2.append(p2)
            x3.append(p3)
        else:
            y1.append(p1)
            y2.append(p2)
            y3.append(p3)
    pi = (6)*(ni/n)
    # Creating figure
    fig = plt.figure()
    ax = plt.axes(projection ="3d")
    # Creating plot
    ax.scatter3D(x1,x2,x3, color = "red")
    ax.scatter3D(y1,y2,y3, color = "blue")
    plt.title("approximation of Pi is "+str(pi)+";"+str(n)+" Dots")
    # show plot
    plt.show()
#algoboule(100)