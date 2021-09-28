# AUSTIN JOHNS AND SHELBY CLOW
# CST-305
# PROJECT 8 NUMERICAL INTEGRATION

from math import sin
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# SETUP FOR SINX + 1 INTEGRATION WITH -PI AND PI AS INTERVAL
f2 = lambda x: sin(x) + 1
a = -1 * np.math.pi;
b = np.math.pi;
N = 4  # FOUR SUBINTERVALS OF DATA
n = 10
f = np.vectorize(f2)

# ASSIGN DATA TO A PLOT
x = np.linspace(a, b, N + 1)
y = f(x)

X = np.linspace(a, b, n * N + 1)
Y = f(X)

# PLOT SETTINGS
plt.figure(figsize=(15, 5))

# SUBPLOT FOR LEFT
plt.subplot(1, 3, 1)
plt.plot(X, Y, 'b')
x_left = x[:-1]  # ENDPOINTS  LEFT
y_left = y[:-1]
plt.plot(x_left, y_left, 'b.', markersize=10)
plt.bar(x_left, y_left, width=(b - a) / N, alpha=0.2, align='edge', edgecolor='b')
plt.title('Left Riemann Sum, N = {}'.format(N))

# SUBPLOT FOR MIDDLE
plt.subplot(1, 3, 2)
plt.plot(X, Y, 'b')
x_mid = (x[:-1] + x[1:]) / 2  # MIDPOINTS
y_mid = f(x_mid)
plt.plot(x_mid, y_mid, 'b.', markersize=10)
plt.bar(x_mid, y_mid, width=(b - a) / N, alpha=0.2, edgecolor='b')
plt.title('Midpoint Riemann Sum, N = {}'.format(N))

# SUBPLOT FOR RIGHT
plt.subplot(1, 3, 3)
plt.plot(X, Y, 'b')
x_right = x[1:]  # ENDPOINTS RIGHT
y_right = y[1:]
plt.plot(x_right, y_right, 'b.', markersize=10)
plt.bar(x_right, y_right, width=-(b - a) / N, alpha=0.2, align='edge', edgecolor='b')
plt.title('Right Riemann Sum, N = {}'.format(N))

# SHOW COMBINED PLOTS
plt.show()

# CALCULATIONS FOR RIEMAN SUM
dx = (b - a) / N
x_left = np.linspace(a, b - dx, N)
x_midpoint = np.linspace(dx / 2, b - dx / 2, N)
x_right = np.linspace(dx, b, N)

# PRINTING DATA
print("Partition with", N, "subintervals.")
left_riemann_sum = np.sum(f(x_left) * dx)
print("Left Riemann Sum:", left_riemann_sum)

midpoint_riemann_sum = np.sum(f(x_midpoint) * dx)
print("Midpoint Riemann Sum:", midpoint_riemann_sum)

right_riemann_sum = np.sum(f(x_right) * dx)
print("Right Riemann Sum:", right_riemann_sum)
