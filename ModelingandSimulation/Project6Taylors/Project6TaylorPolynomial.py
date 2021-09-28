# SHELBY CLOW AND AUSTIN JOHNS
# PROJECT 6 TAYLOR POLYNOMIAL
# CST-305

# PART 1 & 2 - WRITE A PYTHON CODE TO SOLVE THE DIFFERENTIAL EQUATION NUMERICALLY USING TAYLOR SERIES

# IMPORTING PACKAGES
import numpy as np
import sympy as sy
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# _____________PART 1______________

print("----------PART 1----------")
# DEFINES DERIVATIVES TO ADD FIRST/SECOND DERIVATIVE
ddx = [1, -1, 0, -2, -2]
n = 4
print("n = 4.\n")

# TAYLOR POLYNOMIAL THAT CAN BE USED UP TO THE 500TH DEGREE
d = 5
for i in range(500):
    tmp = 2 * (i + 3) * ddx[d - 2]
    ddx.append(tmp)
    d += 1


# RETURNING THE FACTORIAL OF A GIVEN NUMBER (FOR EXPANSION)
def f_(n):
    if n == 1:
        return n
    else:
        return n * f_(n - 1)


# OUTPUT OF TAYLOR POLYNOMIAL ------> ARRAY
def taylor(n, t):
    y = 1
    for i in range(n):
        y = y + (ddx[i + 1] / f_(i + 1)) * t ** (i + 1)
    return y


# CONVERTING TO A FORMAT THAT ODEINT CAN CALCULATE
# RETURNS TAYLOR VALUES
def func(Y, t):
    return [Y[1], 2 * t * Y[1] - (t ** 2) * Y[0]]


y0 = [1, -1]

x = np.linspace(0, 3.5)

# CALCULATING POINTS AT 3.5 AND PRINTING RESULTS
p1 = taylor(n, x)
print(p1)
tVals = odeint(func, y0, x)
print('Value of the point around 3.5: ', tVals[-1][0])
t = 3.5
print('Approximation using Taylor Series at y(3.5) when n = 4', 1 - t - (1 / 3) * t ** 3 - (1 / 12) * t ** 4)

a = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4
b = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4 - (1 / 10) * x ** 5
c = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4 - (1 / 10) * x ** 5 - (1 / 45) * x ** 6
d = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4 - (1 / 10) * x ** 5 - (1 / 45) * x ** 6 - (1 / 42) * x ** 7


# ____________PART 2_______________

print("----------PART 2----------")

# DEFINES DERIVATIVES TO ADD FIRST/SECOND DERIVATIVE
ddx = [1, -1, 0, -2, -2]
n = 8
print("n = 8.\n")

# TAYLOR POLYNOMIAL THAT CAN BE USED UP TO THE 500TH DEGREE
d = 0
for i in range(500):
    tmp = 2 * (i + 3) * ddx[d - 2]
    ddx.append(tmp)
    d += 1


# RETURNING THE FACTORIAL OF A GIVEN NUMBER (FOR EXPANSION)
def f_(n):
    if n == 1:
        return n
    else:
        return n * f_(n - 1)


# OUTPUT OF TAYLOR POLYNOMIAL ------> ARRAY
def taylor(n, t):
    y = 1
    for i in range(n):
        y = y + (ddx[i + 1] / f_(i + 1)) * t ** (i + 1)
    return y


# CONVERTING TO A FORMAT THAT ODEINT CAN CALCULATE
# RETURNS TAYLOR VALUES
def func(Y, t):
    return Y[1], ((x**2) + 4) * Y[1] + Y


y0 = [1, -1]

x = np.linspace(0, 3.5)

# CALCULATING POINTS AT 3.5 AND PRINTING RESULTS
p1 = taylor(n, x)
print(p1)
tVals = odeint(func, y0, x)
print('Value of the point around 3.5: ', tVals[-1][0])
t = 3.5
print('Approximation using Taylor Series at y(3.5) when n = 8', 1 - t - (1 / 3) * t ** 3 - (1 / 12) * t ** 4)

a = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4
b = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4 - (1 / 10) * x ** 5
c = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4 - (1 / 10) * x ** 5 - (1 / 45) * x ** 6
d = 1 - x - (1 / 3) * x ** 3 - (1 / 12) * x ** 4 - (1 / 10) * x ** 5 - (1 / 45) * x ** 6 - (1 / 42) * x ** 7
