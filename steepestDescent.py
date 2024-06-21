from utils import *

def sd(Q,b,c, x, verbose=0):
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
    alpha = dk.T @ dk / (dk.T @ Q @ dk)
    #print("alpha shape", alpha.shape)
    xnew = x + alpha*dk 
    store_x += [xnew]
    counter = 0
    while np.linalg.norm(grad) > 0.000002: #  np.linalg.norm(xnew-x) > 0.000002:
        counter += 1
        x = xnew 
        #print(x_)
        grad = Q@x + b
        #print("grad")
        #print(grad)

        dk = -1*grad 
        alpha = dk.T @ dk / (dk.T @ Q @ dk)
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
    # if verbose >= 3:
    #     plt.scatter(store_x)
        # print("store_x:")

        # for i in store_x:
        #     print(i)
        #     print('-'*40)
    if verbose >= 3:
        #plt.scatter(store_x)
        # print("store_x:")
        x = []
        y = []
        for i in store_x:
            x.append(i[0,0])
            y.append(i[1,0])
        plt.plot(x,y, marker="o",ls="--",markersize=3,markeredgewidth=6, markeredgecolor="y", markerfacecolor="b")

        plt.title('steepest descent')
        plt.ylabel('y', rotation=0)
        plt.xlabel('x')


        plt.show()
        print()


    return xnew, np.linalg.norm(xnew - x), x_, store_x


def sd_with_newtons_method(Q,b,c, x, verbose=0):
    store_x = [x]
    val = (1/2)*(x.T@Q@x + b.T@x + c)

    # calculate gradient Qinv b
    x_ = -1 *np.linalg.inv(Q) @ b
    # print("x*")
    # print(x_)

    grad = Q@x + b
    grad2 = np.linalg.inv(Q)
    #print("grad")
    #print(grad)

    dk = -1*grad 

    alpha = dk.T @ dk / (dk.T @ Q @ dk)
    #print("alpha shape", alpha.shape)
    f1f2 = -1* (grad2@grad)
    
    xnew = x + f1f2 #alpha*dk 
    store_x += [xnew]
    counter = 0
    while np.linalg.norm(grad) > 0.000002:
        counter += 1
        x = xnew 
        #print(x_)
        grad = Q@x + b
        #print("grad")
        #print(grad)

        dk = -1*grad 
        alpha = dk.T @ dk / (dk.T @ Q @ dk)
        f1f2 = -1* (grad2@grad)

        xnew = x + f1f2 #alpha*dk
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
    # if verbose >= 3:
    #     plt.scatter(store_x)
        # print("store_x:")

        # for i in store_x:
        #     print(i)
        #     print('-'*40)
    if verbose >= 3:
        #plt.scatter(store_x)
        # print("store_x:")
        x = []
        y = []
        for i in store_x:
            x.append(i[0,0])
            y.append(i[1,0])
        plt.plot(x,y, marker="o",ls="--",markersize=3,markeredgewidth=6, markeredgecolor="y", markerfacecolor="b")

        plt.title("steepest descent with newton's method")
        plt.ylabel('y', rotation=0)
        plt.xlabel('x')


        plt.show()
        print()


    return xnew, np.linalg.norm(xnew - x), x_, store_x