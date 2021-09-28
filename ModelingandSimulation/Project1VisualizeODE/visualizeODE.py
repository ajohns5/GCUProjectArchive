# AUSTIN JOHNS AND SHELBY CLOW
# CST-305

# Import the required modules
import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

k = float(input("Please enter the number of processors: "))
f = float(input("Please input the percentage of the process that was parallelized: "))


# Define a function which calculates the derivative
# function that returns dS/df
def model(f, k):
    dSdf = 1 / ((1 - (f/100)) + ((f/100) / k))
    print("Maximum speedup per parallelization percentage: ", dSdf)
    return dSdf

# initial condition
x0 = 0.1

# time points
t = np.linspace(0.1, 45)

# solve ODE
x = odeint(model, x0, t)

# plot results
plt.plot(t, x)
plt.xlabel('Speedup')
plt.ylabel('f(S)')
plt.show()
