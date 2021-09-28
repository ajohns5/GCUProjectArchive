import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# DEFINING THE PARAMETERS OF THE LORENZ FUNCTINO
sigma, beta, rho = 10, 2.667, 24

# REQUESTING DATA FROM THE USER
u0 = input("Please enter file size of file x: ")
v0 = input("Please enter file size of file y: ")
w0 = input("Please enter file size of file z: ")

# DEFINING THE MAXIMUM TIME POINT AND AMOUNT OF POINTS
tmax, n = 100, 10000

# DEFINING THE LORENZ FUNCTION
def lorenz(X, t, sigma, beta, rho):
    u, v, w = X
    up = -sigma * (u - v)
    vp = rho * u - v - u * w
    wp = -beta * w + u * v
    return up, vp, wp


# LORENZ FUNCTION INTEGRATED AT THE TIME POINTS
t = np.linspace(0, tmax, n)
f = odeint(lorenz, (u0, v0, w0), t, args=(sigma, beta, rho))
x, y, z = f.T

# PLOTTING THE LORENZ FUNCTION IN 3 DIMENTIONAL SPACE
fig = plt.figure()
ax = fig.gca(projection='3d')

# LINE DESIGN
s = 10
c = np.linspace(0, 1, n)
for i in range(0, n - s, s):
    ax.plot(x[i:i + s + 1], y[i:i + s + 1], z[i:i + s + 1], color=(1, c[i], 0), alpha=0.4)

# PLOT THE GRAPH AT A DEFINED ANGLE TO VIEW X-Z AXIS
ax.view_init(180, 90)
# PLOT SETUP
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
ax.set_zlabel("Z Axis")
# PLOT OUTPUT
plt.show()


