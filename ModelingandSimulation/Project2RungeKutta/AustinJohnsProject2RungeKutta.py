# Shelby Clow and Austin Johns
# CST-305
# Runge-Kutta method of solving an ODE, computational steps, and computation time

# import required packages for time, math, and plotting
import math
import matplotlib.pyplot as plt
import time

# starts timer for computation time
start_time = time.time()


# finds values for new x and y using runge kutta method of 4th order ODE
def runge_kutta(f, x0, y0, h):
    k0 = f(x0, y0)
    k1 = f(x0 + h / 2, y0 + h / 2 * k0)
    k2 = f(x0 + h / 2, y0 + h / 2 * k1)
    k3 = f(x0 + h, y0 + h * k2)
    k = 1 / 6 * (k0 + 2.0 * k1 + 2.0 * k2 + k3)

    x1 = x0 + h
    y1 = y0 + h * k
    return x1, y1


# function to calculate ODE with x and y values
def f(x, y):
    return ((y) / (math.exp(x) - 1))


# main to use ODE and values for x and y. Loop is used to find  up to (x1000, y1000)
if __name__ == "__main__":
    x0 = 1.0
    y0 = 5.0
    h = 0.02

    x_values = [x0]
    y_values = [y0]

    x = x0
    y = y0
    for i in range(1001):
        x, y = runge_kutta(f, x, y, h)
        x_values.append(x)
        y_values.append(y)
        print("(x", i, ",y", i, ") = (", x, ",", y, ")")
    print("Computation Steps: ", i * 7)
    print("Computing Time: %s seconds" % (time.time() - start_time))
    plt.plot(x_values, y_values)
    plt.show()
