from utils import * 

from steepestDescent import sd , sd_with_newtons_method
from gradientDescent import gd 


##########################################
#               INITIALIZE               #
##########################################
Q = np.array([[5,1], [1, 2]])
thresh= 2/5.30277564
# 0.3771609692315777
b = np.array([[-2], [3]])
c = 10
x = np.array([[1], [0]])
x = np.array([[10], [10]])

alpha = 0.002

alpha = 0.1
# alpha = 0.3771609692315777 - 0.00002

no_of_pts = 10

if __name__ == "__main__":
    final_x, cost, x_star, store_x= gd(Q, b, c, x, alpha, verbose=3)
    #final_x, cost, x_star, store_x= sd(Q, b, c, x, verbose=3)
    #final_x, cost, x_star, store_x= sd_with_newtons_method(Q, b, c, x, verbose=3)


    # Draws 3D plot of descent
    plot_descent(10,final_x, cost, x_star, store_x)