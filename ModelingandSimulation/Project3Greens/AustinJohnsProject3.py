# SHELBY CLOW AND AUSTIN JOHNS
# CST-305
# PROJECT 3: GREEN'S FUNCTION AND ODE WITH IVP

# IMPORTING REQUIRED PACKAGES
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt2
import sympy as sy
from numpy import *
import time

# DECLARING VALUES FOR EQUATION PROCESS
x = sy.symbols("x")
t = arange(0.0, 10.0, 0.1)


# FUNCTION FOR FIRST EQUATION
def equation_one(t):
    # FIRST EQUATION IN SYMPY
    eq = sy.Poly((x ** 2) + (2 * x) + 0, x)

    # COEFFICIENT EXTRACTION
    ans = eq.all_coeffs()

    # INITIALIZES Q1 AND Q2 VARIABLES FOR USE AS LAMBDA1 AND LAMBDA2
    lambda1 = 1.0
    lambda2 = 1.0

    # VALUES OF COEFFICIENTS AS FLOATS
    a = float(ans[0])
    b = float(ans[1])
    c = float(ans[2])
    temp = 0

    # STORES b^2 - 4ac FOR PROCESSING OF POTENTIAL IMAGINARY
    d = b * b - 4 * a * c
    if (d < 0):
        # D MUST BE POSITIVE TO BE CALCULATED
        temp = d
        d = -d

    # LAMBDA1 AND LAMBDA2 CALCULATIONS
    lambda1 = (-b + sqrt(d)) / (2 * a)
    lambda2 = (-b - sqrt(d)) / (2 * a)
    print("Equation 1 Lambda 1:", lambda1)
    print("Equation 1 Lambda 2:", lambda2)

    # CASE DETERMINATION
    if (lambda1 == lambda2):
        case = 3
    elif (temp < 0):
        case = 2
    elif (lambda1 != lambda2):
        case = 1

    return caseStatement(lambda1, lambda2, case, t)


def equation_two(t):
    # SECOND EQUATION IN SYMPY
    eq = sy.Poly((x ** 2) + (0 * x) + (1), x)

    # EXTRACTION OF COEFFICIENTS
    ans = eq.all_coeffs()

    # COEFFICIENTS AS FLOATS
    a = float(ans[0])
    b = float(ans[1])
    c = float(ans[2])
    temp = 0

    # STORES b^2 - 4ac FOR POSSIBLE IMAGINARY
    d = b * b - 4 * a * c
    if (d < 0):
        # D MUST BE POSITIVE
        temp = d
        d = -d

    # LAMBDA CALCULATION
    lambda1 = (-b + sqrt(d)) / (2 * a)
    lambda2 = (-b - sqrt(d)) / (2 * a)

    print("Equation 2 Lambda 1:", lambda1)
    print("Equation 2 Lambda 2:", lambda2)

    # CASE DETERMINATION
    if (lambda1 == lambda2):
        case = 3
    elif (temp < 0):
        case = 2
    elif (lambda1 != lambda2):
        case = 1

    return caseStatement(lambda1, lambda2, case, t)


# SOLUTION CALCULATION DETERMINED BY CASE
def caseStatement(lambda1, lambda2, case, t):
    if (case == 1):
        # CASE 1 CALCULATION
        return (-.5 * exp(2 * t) * exp(lambda1 * t)) + (.5 * exp(lambda2 * t))
    elif (case == 2):
        # CASE 2 CALCULATION
        return (-sin(t) * exp(0 * t) * cos(lambda1 * t)) + (
                    (cos(t) / (-sin(t) * sin(-t) + cos(t) ** 2)) * exp(0 * t) * sin(lambda2 * t))
    elif (case == 3):
        # CASE 3 CALCULATION
        return 3
    # RETURNS 0 IF NO CASE REQUIREMENTS ARE MET, ERROR CHECKING
    return 0


# EQUATION 1 GREEN'S VALUE
def green_one(t):
    return t - 2 * (2 - exp(-2 * t))


# EQUATION 2 GREEN'S VALUE
def green_two(t):
    return -1 * (-1 + cos(t))


# GREEN'S FUNCTION AND HOMOLOGOUS PLOT
plt1.plot(t, green_one(t), 'g-', linewidth=2, label='Homogeneous')
plt1.plot(t, equation_one(t), 'b--', linewidth=2, label='Green\'s')
plt1.xlabel("t")
plt1.ylabel("y")
plt1.title("Green's Function and\n Homogeneous Equation Visualization")

# PLOT SETUP
print("Graph for Equation One:")
plt1.legend()
plt1.show()

# GREEN'S FUNCTION AND HOMOLOGOUS PLOT
plt2.plot(t, green_two(t), 'g-', linewidth=2, label='Homogeneous')
plt2.plot(t, equation_two(t), 'b--', linewidth=2, label='Green\'s')
plt1.xlabel("t")
plt1.ylabel("y")
plt1.title("Green's Function and\n Homogeneous Equation Visualization")

# LEGEND SETUP
print("Graph for Equation Two:")
plt2.legend()
plt2.show()
