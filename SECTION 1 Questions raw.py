#Section 1 Questions 

#Question 1:

def relative_error(true_value, approx_value):
    # Ensure that true_value is not zero to avoid division by zero
    if true_value == 0:
        raise ValueError("true_value cannot be zero for relative error calculation.")
    
    # Calculate the relative error
    error = abs(true_value - approx_value) / abs(true_value)

    return error

# Example usage:
true_value = 10.0
approx_value = 9.5

error = relative_error(true_value, approx_value)
print(f"Relative Error: {error}")



#Question 2:

import numpy as np
def solve_linear_system(A, b):
    # Use numpy.linalg.solve to find the solution
    x = np.linalg.solve(A, b)
    
    return x

# Example usage:
A = np.array([[-1, 1, 1],
              [1,  -1, 1],
              [1,  1, -1]])

b = np.array([1, 2, 3])

# Solve the system
solution = solve_linear_system(A, b)

print("Coefficient Matrix A:")
print(A)

print("\nRight-hand side Vector b:")
print(b)

print("\nSolution Vector x:")
print(solution)



#Question 3

def bisection_method(func, a, b, tolerance):
    
    if func(a) * func(b) > 0:
        raise ValueError("The function values at the interval endpoints must have opposite signs.")

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2
        if func(c) == 0:
            return c
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c

    return (a + b) / 2

# Example usage:
def quadratic_function(x):
    return x**2 - 4

# Find the root of the quadratic function within the interval [0, 3] with tolerance 0.0001
root = bisection_method(quadratic_function, 0, 3, 0.0001)
print("Approximate Root:", root)



#Question 4

def euler_method(func, y0, x0, h, n):
    y = y0
    x = x0

    for _ in range(n):
        y += h * func(y, x)
        x += h

    return y

# Example usage:
def ode_func(y, x):
    return x * y

# Solve the ODE dy/dx = x * y with initial condition y(0) = 1, step size h = 0.1, and number of steps n = 10
result = euler_method(ode_func, 1, 0, 0.1, 10)
print("Approximate value of y at x0 + n*h:", result)


