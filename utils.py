import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from mpl_toolkits import mplot3d

def cost_func(X2, Y2):
    return (5/2)* (X2*2)+(Y2*2)+X2*Y2-2*X2+3*Y2+10

def n_pts(px, py, i, j, n=10):
    # px = 1
    # py = 1.2 
    # i = 11
    # j = 1.2 
    X = []
    Y = []
    slope = (j-py)/(i-px)
    step = (px-i)/(n+1)
    for c in range(0,n):
        current_x = i  + c*step 
        current_y = j + slope*(current_x-i)
        X.append(current_x)
        Y.append(current_y)
    return X, Y

def plot_descent(no_of_pts, final_x, cost, x_star, store_x):

    ax = plt.axes(projection = "3d")
    X1 = []
    Y1 = []
    for i,j  in store_x:
        X1.append(i[0])
        Y1.append(j[0])
    # x1 -.2  0.3
    # y1 0.1  0.02


    # pts in between 
    if no_of_pts != 0:
        X2 = []
        Y2 = []
        for i,j in zip(X1, Y1):
            # 
            if X2 == []:
                # first time 
                X2.append(i)
                Y2.append(j)
                px = i 
                py = j 
            else:
                # find distance from last to current 
                l,m= n_pts(px, py, i,j,n=no_of_pts)
                X2 += l 
                Y2 += m 
                px = i 
                py = j
        X2 = np.array(X2)
        Y2 = np.array(Y2)
        Z2 = cost_func(X2, Y2)

    X1 = np.array(X1)
    Y1 = np.array(Y1)
    Z1 = cost_func(X1, Y1)




    x = np.arange(-10,10,0.1)
    y = np.arange(-10,10,0.1)
    X,Y = np.meshgrid(x,y)

    # Z = (5/2)* (X*2)+(Y*2)+X*Y-2*X+3*Y+10
    Z = cost_func(X, Y)

    #ax.scatter(X, Y, Z, marker="v", alpha=0.008, c='blue')
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.scatter(X1, Y1, Z1, marker=".", c='green')

    if no_of_pts != 0:
        ax.scatter(X2, Y2, Z2 , c='red', alpha=0.8, marker='.')

    # Starting Point
    a = X1[0]
    b = Y1[0]
    z_star = (5/2)* (a*2)+(b*2)+a*b-2*a+3*b+10
    ax.scatter(a, b, z_star, marker='s', c='Red' )

    # Final Point
    a = x_star[0,0]
    b = x_star[1,0]
    z_star = (5/2)* (a*2)+(b*2)+a*b-2*a+3*b+10
    ax.scatter(a, b, z_star, marker='s', c='black' )

    plt.show()