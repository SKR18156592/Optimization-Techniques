from utils import *

def gd(Q,b,c, x,alpha, verbose=0):
    store_x = [x]
    val = (1/2)*(x.T@Q@x + b.T@x + c)

    # calculate gradient Qinv b
    x_ = -1 *np.linalg.inv(Q) @ b
    # print("x*")
    # print(x_)
    grad = Q@x + b
    #print("grad")
    #print(grad)

    dk = -1*grad 
    #alpha = dk.T @ dk / (dk.T @ Q @ dk)
    #print("alpha shape", alpha.shape)
    xnew = x + alpha*dk 
    store_x += [xnew]

    counter = 0
    while np.linalg.norm(grad) > 0.000002:
        counter += 1
        #print(counter)
        x = xnew 
        #print(x_)
        grad = Q@x + b
        #print("grad")
        #print(grad)

        dk = -1*grad 
        #alpha = dk.T @ dk / (dk.T @ Q @ dk)
        xnew = x + alpha*dk 
        store_x += [xnew]
        if verbose > 10:
            print("Reached: ", (xnew[0,0], xnew[1,0]))

    print()
    print(f"Finished in {counter} steps")
    final_x, cost, x_star, store_x = xnew, np.linalg.norm(xnew - x), x_, store_x

    if verbose >= 1:
        print("#"*40)
        print("OUTPUT".center(40))
        print("#"*40)

        print("Final pos:")
        print(final_x)
        print()
    if verbose >= 2:
        print("x*:")
        print(x_star)
        print()
    if verbose >= 3:
        #plt.scatter(store_x)
        # print("store_x:")
        x = []
        y = []
        for i in store_x:
            x.append(i[0,0])
            y.append(i[1,0])
        plt.plot(x,y, marker="o",ls="--",markersize=3,markeredgewidth=6, markeredgecolor="y", markerfacecolor="b")
        plt.show()
        print()

    return xnew, np.linalg.norm(xnew - x), x_, store_x